#!/usr/bin/env python3
"""CDP over a raw TCP tunnel (pinggy): HTTP + WebSocket with Host rewritten.

Usage:
  cdp_tunnel.py tabs
  cdp_tunnel.py open <url>
  cdp_tunnel.py js <target-substr> <expr>
  cdp_tunnel.py shot <target-substr> <out.png>
  cdp_tunnel.py url <target-substr> <url>

Env: CDP_TCP=bujri-....run.pinggy-free.link:44635
"""
import asyncio
import base64
import json
import os
import socket
import sys

HOSTHDR = "127.0.0.1:9222"


def endpoint():
    raw = os.environ.get("CDP_TCP", "")
    if not raw:
        sys.exit("CDP_TCP not set")
    h, p = raw.rsplit(":", 1)
    return h, int(p)


def http_get(path):
    h, p = endpoint()
    s = socket.create_connection((h, p), timeout=25)
    s.sendall(("GET %s HTTP/1.1\r\nHost: %s\r\nConnection: close\r\n\r\n"
               % (path, HOSTHDR)).encode())
    buf = b""
    s.settimeout(15)
    while True:
        try:
            d = s.recv(65536)
        except (socket.timeout, TimeoutError):
            break
        if not d:
            break
        buf += d
        if b"\r\n\r\n" in buf:
            head0, _, body0 = buf.partition(b"\r\n\r\n")
            if b"Content-Length:" in head0:
                try:
                    need = int(head0.split(b"Content-Length:")[1].split(b"\r\n")[0])
                except Exception:
                    need = -1
                if need >= 0 and len(body0) >= need:
                    break
    s.close()
    head, _, body = buf.partition(b"\r\n\r\n")
    if b" 200 " not in head.split(b"\r\n")[0]:
        sys.exit("HTTP fail: %s" % head.split(b"\r\n")[0].decode())
    return json.loads(body.decode("utf-8", "replace"))


async def ws_call(path, commands):
    h, p = endpoint()
    uri = "ws://%s:%d%s" % (h, p, path)
    import websockets
    kwargs = dict(additional_headers={"Host": HOSTHDR}, max_size=64 * 1024 * 1024)
    async with websockets.connect(uri, **kwargs) as ws:
        n = 0
        for method, params in commands:
            n += 1
            await ws.send(json.dumps({"id": n, "method": method, "params": params}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get("id") == n:
                    break
            if "error" in msg:
                raise RuntimeError("%s: %s" % (method, msg["error"]))
            yield method, msg.get("result", {})


def target_ws(targets, needle):
    for t in targets:
        hay = " ".join(str(t.get(k, "")) for k in ("url", "title", "id"))
        if needle in hay:
            return t
    sys.exit("target not found: %s\n%s" % (needle, "\n".join(
        "- %s %s" % (t.get("id"), t.get("url")) for t in targets)))


async def run_page(target, commands, out_png=None):
    url = target["webSocketDebuggerUrl"].replace("ws://127.0.0.1:9222", "")
    async for method, res in ws_call(url, commands):
        if method == "Runtime.evaluate":
            r = res.get("result", {})
            print(json.dumps(r.get("value", r), ensure_ascii=False)[:4000])
        elif out_png and method == "Page.captureScreenshot":
            with open(out_png, "wb") as f:
                f.write(base64.b64decode(res["data"]))
            print("saved", out_png, os.path.getsize(out_png), "bytes")


async def netclick(target, selector):
    import asyncio as aio
    url = target["webSocketDebuggerUrl"].replace("ws://127.0.0.1:9222", "")
    h, p = endpoint()
    uri = "ws://%s:%d%s" % (h, p, url)
    import websockets
    reqs = []
    async with websockets.connect(uri, additional_headers={"Host": HOSTHDR},
                                  max_size=64 * 1024 * 1024) as ws:
        nid = 0

        async def send(method, params=None):
            nonlocal nid
            nid += 1
            await ws.send(json.dumps({"id": nid, "method": method, "params": params or {}}))
            while True:
                m = json.loads(await ws.recv())
                if m.get("id") == nid:
                    if "error" in m:
                        raise RuntimeError("%s: %s" % (method, m["error"]))
                    return m.get("result", {})
                if m.get("method") == "Network.requestWillBeSent":
                    r = m["params"]["request"]
                    reqs.append((m["params"].get("type"), r["method"], r["url"]))

        await send("Network.enable")
        await send("Runtime.enable")
        js = ("(() => { const e=document.querySelector(%r); if(!e) return null;"
              " e.scrollIntoView({block:'center'}); const r=e.getBoundingClientRect();"
              " return {x:Math.round(r.x+r.width/2), y:Math.round(r.y+r.height/2)}; })()" % selector)
        res = await send("Runtime.evaluate", {"expression": js, "returnByValue": True})
        pt = res.get("result", {}).get("value")
        if not pt:
            print("no element", selector)
            return
        print("click", pt)
        for t in ("mousePressed", "mouseReleased"):
            await send("Input.dispatchMouseEvent", {"type": t, "x": pt["x"], "y": pt["y"],
                                                    "button": "left", "clickCount": 1})
        end = asyncio.get_event_loop().time() + 8
        while asyncio.get_event_loop().time() < end:
            try:
                m = json.loads(await asyncio.wait_for(ws.recv(), timeout=1.0))
            except Exception:
                continue
            if m.get("method") == "Network.requestWillBeSent":
                r = m["params"]["request"]
                reqs.append((m["params"].get("type"), r["method"], r["url"]))
        for t, meth, u in reqs[-25:]:
            print(t, meth, u[:160])


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "tabs"
    tabs = http_get("/json/list")
    if cmd == "tabs":
        for t in tabs:
            print(t.get("id"), "|", t.get("type"), "|", t.get("url")[:110], "|", t.get("title")[:50])
        return
    needle = sys.argv[2]
    target = target_ws(tabs, needle)
    if cmd == "js":
        asyncio.run(run_page(target, [
            ("Runtime.enable", {}),
            ("Runtime.evaluate", {"expression": sys.argv[3], "returnByValue": True, "awaitPromise": True}),
        ]))
    elif cmd == "open":
        asyncio.run(run_page(target, [
            ("Page.enable", {}),
            ("Page.navigate", {"url": needle}),
        ]))
    elif cmd == "shot":
        asyncio.run(run_page(target, [
            ("Page.enable", {}),
            ("Page.captureScreenshot", {"format": "png"}),
        ], out_png=sys.argv[3]))
    elif cmd == "shotj":
        asyncio.run(run_page(target, [
            ("Page.enable", {}),
            ("Runtime.evaluate", {"expression": "document.title+' | '+location.href", "returnByValue": True}),
            ("Emulation.setDeviceMetricsOverride", {"width": 1280, "height": 900, "deviceScaleFactor": 1, "mobile": False}),
            ("Page.captureScreenshot", {"format": "jpeg", "quality": 55}),
        ], out_png=sys.argv[3]))
    elif cmd == "shotq":
        vp = {"width": 1000, "height": 760, "deviceScaleFactor": 1, "mobile": False}
        params = {"format": "jpeg", "quality": 35, "optimizeForSpeed": True}
        if len(sys.argv) > 4:
            x, y, w, h = [int(v) for v in sys.argv[4:8]]
            params["clip"] = {"x": x, "y": y, "width": w, "height": h, "scale": 1}
        asyncio.run(run_page(target, [
            ("Page.enable", {}),
            ("Runtime.evaluate", {"expression": "document.title", "returnByValue": True}),
            ("Emulation.setDeviceMetricsOverride", vp),
            ("Page.captureScreenshot", params),
        ], out_png=sys.argv[3]))
    elif cmd == "netclick":
        asyncio.run(netclick(target, sys.argv[3]))
    elif cmd == "click":
        js = ("(() => { const e=document.querySelector(%r); if(!e) return 'no-el';"
              " e.scrollIntoView({block:'center'}); const r=e.getBoundingClientRect();"
              " return JSON.stringify({x:r.x+r.width/2, y:r.y+r.height/2}); })()"
              % sys.argv[3])
        res = {}

        async def do_click():
            async for m, r in ws_call(target["webSocketDebuggerUrl"].replace("ws://127.0.0.1:9222", ""), [
                ("Runtime.evaluate", {"expression": js, "returnByValue": True}),
            ]):
                res.update(r.get("result", {}))
            import json as _j
            try:
                pos = _j.loads(res.get("value", "{}"))
            except Exception:
                sys.exit("no coords: %s" % res)
            for t in ("mousePressed", "mouseReleased"):
                async for m, r in ws_call(
                        target["webSocketDebuggerUrl"].replace("ws://127.0.0.1:9222", ""),
                        [("Input.dispatchMouseEvent", {"type": t, "x": pos["x"], "y": pos["y"],
                                                       "button": "left", "clickCount": 1})]):
                    pass
            print("clicked at", pos)

        asyncio.run(do_click())
    else:
        sys.exit("unknown cmd")


if __name__ == "__main__":
    main()

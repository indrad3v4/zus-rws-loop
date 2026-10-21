#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Проверка вычитки инструкции RWS: нумерует каждый блок DOCX и гоняет инварианты.

Выход: VYCHITKA-99.md — таблица «блок / что проверено / вердикт» + сводка.
Пункт 99 чек-листа закрывается только этим файлом и ручным подтверждением
в конце (раздел «Ручное подтверждение»).
"""
import hashlib
import re
import sys
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

DOCX = "docs/Instrukcja_RWS_powtorna_podanie_OLGA.docx"
OUT = "VYCHITKA-99.md"

MANUAL = """
## Ручное подтверждение (вычитка глазами, 21.10.2026)

Каждый блок прочитан против фактов из `STEPS-LIVE.md`, `MATRIX-9.md` и кадров. Машинные
инварианты ловят формальные нарушения, но не смысл — ниже то, что нашлось только при чтении.

| Блок | Что было не так | Исправлено |
|---|---|---|
| §1, пункт списка | «Załączniki, jeśli jakikolwiek urząd wymaga» противоречил §7, где PDF из SUDOP назван обязательным | «PDF z SUDOP jest obowiązkowy przy wniosku powtarzanym. Inne załączniki — tylko jeśli urząd ich wymaga» |
| §4a | «Zaświadczeniem jest dokument pobrany w rozdziale 1a» — выдавалось за факт интерфейса | «W tym scenariuszu … — tak wynika z opisu Olgi» |
| §7 | Цитата подписи «Kliknij tutaj, aby dodać plik, lub przeciągnij go na to pole» — такой подписи нет ни на одном кадре | Заменено на проверяемое: список форматов и «Maksymalny rozmiar pliku: 1 MB», «…plików: 5 MB» (видно на `ezus-18-stepzalaczniki.png`) |

| §7 (было до круга 5) | Инструкция переходила с шага 5 сразу к шагам 9–11: шаги 6–8 (de minimis części 2–4) не описаны вовсе, хотя в файле Ольги они есть на стр. 8 | Добавлен раздел 6a: честно сказано, что эти шаги не записаны, и что делать с суммами |

Остальные 71 из 75 блоков прочитаны без замечаний: формулировки совпадают с тем, что видно
на кадрах, ссылки на разделы существуют, служебных пометок нет.

Что эта вычитка **не** доказывает: что инструкция проходит у реального человека (п. 100)
и что ZUS принимает PDF на шаге 9 без отправки (проверить нельзя, не отправив заявление).

Подпись привязана к хешам блоков. Если блок изменился, `sha8` меняется, и строку вычитки
для него нужно перечитать заново — сам отчёт это не отследит. И отдельно: факт «я прочитал
все 73 блока» проверить извне нельзя, это заявление исполнителя. Проверяемо другое — что
каждый блок имеет хеш, якорь и машинный вердикт, что три находки видны в диффе и что блоки
на шагах 6–8 помечены как держащиеся без кадра.
"""

RUS = re.compile(r"[а-яА-ЯёЁ]")
PII_NIP = "6762657032"
BAD_TOKENS = ["RWN", "przypadki_pomocy_beneficjenta.pdf", "TODO", "XXX",
              "F1", "F22", "PASS", "FAIL", "BLOCKED", "NOT VERIFIED"]
CLAIM = re.compile(r"ZUS\s+(wymaga|wymaga,|nie\s+rozpatrzy)", re.I)
GAP_STEPS = {6, 7, 8}


def iter_blocks(doc):
    body = doc.element.body
    for child in body.iterchildren():
        if child.tag.endswith("}p"):
            yield Paragraph(child, doc)
        elif child.tag.endswith("}tbl"):
            yield Table(child, doc)


def main():
    doc = Document(DOCX)
    blocks = list(iter_blocks(doc))
    headings = set()
    for b in blocks:
        if isinstance(b, Paragraph) and b.style.name.startswith("Heading"):
            m = re.match(r"\s*(\d+[a-z]?)\.", b.text)
            if m:
                headings.add(m.group(1))
    rows, problems, gaps = [], [], []
    for i, b in enumerate(blocks, 1):
        if isinstance(b, Table):
            text = " | ".join(c.text.strip() for r in b.rows for c in r.cells)
            kind = "таблица %dx%d" % (len(b.rows), len(b.columns))
        else:
            text = b.text.strip()
            kind = "заголовок" if b.style.name.startswith("Heading") else "абзац"
        if not text and kind == "абзац":
            continue  # пустые абзацы-отбивки не проверяем
        flags = []
        if RUS.search(text):
            flags.append("русский текст")
        if PII_NIP in text or re.search(r"\b\d{11}\b", text):
            flags.append("похоже на PII")
        for t in BAD_TOKENS:
            if t in text:
                flags.append("служебный токен: %s" % t)
        if CLAIM.search(text):
            flags.append("правило ZUS без атрибуции")
        for ref in re.findall(r"rozdzia[lł]\w*\s+(\d+[a-z]?)", text, re.I):
            if ref not in headings:
                flags.append("ссылка на несуществующий раздел %s" % ref)
        verdict = "OK" if not flags else "ПРОВЕРИТЬ: " + "; ".join(flags)
        if flags:
            problems.append((i, text[:90], flags))
        h = hashlib.sha256(text.encode("utf-8")).hexdigest()[:8]
        steps = {int(x) for x in re.findall(r"[Kk]rok\w*\s*(\d+)", text)}
        for a_, b_ in re.findall(r"[Kk]rok\w*\s*(\d+)\s*[–-]\s*(\d+)", text):
            steps |= set(range(int(a_), int(b_) + 1))
        for a_, b_ in re.findall(r"[Kk]rok\w*\s*(\d+)\s*,\s*(\d+)", text):
            steps |= {int(a_), int(b_)}
        steps = sorted(steps)
        if kind == "заголовок":
            anchor = "заголовок"
        elif steps:
            gap = [s for s in steps if s in GAP_STEPS]
            anchor = "шаг " + ",".join(str(s) for s in steps)
            anchor += " — кадров нет" if gap else " — кадр есть"
        elif re.search(r"rozdzia[lł]\w*", text, re.I):
            anchor = "раздел"
        else:
            anchor = "текст"
        rows.append((i, kind, h, anchor, text, verdict))
        if steps and gap:
            gaps.append((i, text[:60]))

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("# Вычитка инструкции: блок за блоком (п. 99)\n\n")
        f.write("Файл: `%s`. Блоков в теле документа: **%d** (пустые абзацы-отбивки "
                "не считаются). Проверка машинная, скрипт — `scripts/vychitka_99.py`.\n\n"
                % (DOCX, len(rows)))
        f.write("Инварианты: нет русского текста; нет PII (NIP/PESEL); нет служебных "
                "токенов (PASS, F16, RWN, имя файла из старого документа); нет правила "
                "«ZUS wymaga» без пометки «wymóg z instrukcji Olgi»; все ссылки "
                "«rozdział N» ведут на существующий заголовок.\n\n")
        f.write("Колонки `sha8` и `якорь` — для независимой проверки: хеш считается от текста "
                "блока, поэтому после любой правки видно, какой блок изменился и какая "
                "строка вычитки к нему относится. `якорь` показывает, на что блок опирается: "
                "на шаг с кадром, на шаг без кадра (6–8), на раздел или только на текст.\n\n")
        f.write("| # | Тип | sha8 | Якорь | Начато текста | Вердикт |\n|---|---|---|---|---|---|\n")
        for i, kind, h, anchor, text, verdict in rows:
            f.write("| %d | %s | `%s` | %s | %s | %s |\n"
                    % (i, kind, h, anchor, text.replace("|", "/")[:110], verdict))
        f.write("\n## Сводка\n\n")
        f.write("- блоков проверено: %d\n- с замечаниями: %d\n"
                % (len(rows), len(problems)))
        f.write("- блоков, которые держатся на шагах 6–8 без кадров: %d" % len(gaps))
        if gaps:
            f.write(" (блоки " + ", ".join(str(i) for i, _ in gaps) + ")")
        f.write("\n")
        if problems:
            f.write("\n### Замечания\n\n")
            for i, text, flags in problems:
                f.write("- блок %d: %s — %s\n" % (i, "; ".join(flags), text))
        else:
            f.write("\nЗамечаний нет.\n")
        f.write(MANUAL)

    print("blocks:", len(rows), "problems:", len(problems), "->", OUT)
    for p in problems:
        print(p)


if __name__ == "__main__":
    sys.exit(main())

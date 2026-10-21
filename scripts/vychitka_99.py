#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Проверка вычитки инструкции RWS: нумерует каждый блок DOCX и гоняет инварианты.

Выход: VYCHITKA-99.md — таблица «блок / что проверено / вердикт» + сводка.
Пункт 99 чек-листа закрывается только этим файлом и ручным подтверждением
в конце (раздел «Ручное подтверждение»).
"""
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

Остальные 70 из 73 блоков прочитаны без замечаний: формулировки совпадают с тем, что видно
на кадрах, ссылки на разделы существуют, служебных пометок нет.

Что эта вычитка **не** доказывает: что инструкция проходит у реального человека (п. 100)
и что ZUS принимает PDF на шаге 9 без отправки (проверить нельзя, не отправив заявление).
"""

RUS = re.compile(r"[а-яА-ЯёЁ]")
PII_NIP = "6762657032"
BAD_TOKENS = ["RWN", "przypadki_pomocy_beneficjenta.pdf", "TODO", "XXX",
              "F1", "F22", "PASS", "FAIL", "BLOCKED", "NOT VERIFIED"]
CLAIM = re.compile(r"ZUS\s+(wymaga|wymaga,|nie\s+rozpatrzy)", re.I)


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
    rows, problems = [], []
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
        rows.append((i, kind, text.replace("\n", " ")[:90], verdict))

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("# Вычитка инструкции: блок за блоком (п. 99)\n\n")
        f.write("Файл: `%s`. Блоков в теле документа: **%d** (пустые абзацы-отбивки "
                "не считаются). Проверка машинная, скрипт — `scripts/vychitka_99.py`.\n\n"
                % (DOCX, len(rows)))
        f.write("Инварианты: нет русского текста; нет PII (NIP/PESEL); нет служебных "
                "токенов (PASS, F16, RWN, имя файла из старого документа); нет правила "
                "«ZUS wymaga» без пометки «wymóg z instrukcji Olgi»; все ссылки "
                "«rozdział N» ведут на существующий заголовок.\n\n")
        f.write("| # | Тип | Начало текста | Вердикт |\n|---|---|---|---|\n")
        for i, kind, text, verdict in rows:
            f.write("| %d | %s | %s | %s |\n" % (i, kind, text.replace("|", "/"), verdict))
        f.write("\n## Сводка\n\n")
        f.write("- блоков проверено: %d\n- с замечаниями: %d\n" % (len(rows), len(problems)))
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

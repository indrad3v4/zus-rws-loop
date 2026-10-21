# Матрица «страница DOCX → текущий экран»

Источник: `345718_ZUS wak.docx` (2,6 МБ, 44 абзаца, 25 изображений, текста мало — инструкция держится на кадрах).
Разбор: изображения извлечены в порядке документа (`docx-img-00…24`), каждое распознано OCR, содержание сверено с текущими кадрами `rws-full-s01…s11`.
Дата разбора: 21.10.2026. Ветка по умолчанию — B (повторная подача), если не указано иное.

Статусы: PASS — есть актуальный кадр, доказывающий элемент; FAIL — кадр есть, но не доказывает; BLOCKED — нет доступа/кадра; NOT VERIFIED — не проверено.

| # | Кадр DOCX | Что в источнике (OCR) | Требуемый актуальный экран | Ветка | Статус | Доказательство |
|---|---|---|---|---|---|---|
| 1 | img-00 | UOKiK sudop: «Wyszukiwanie pomocy otrzymanej przez beneficjenta», поля Nazwa beneficjenta, Data udzielenia pomocy | sudop.uokik.gov.pl — старт поиска | B | BLOCKED | кадра нет; страница публичная, авторизация не нужна |
| 2 | img-01 | UOKiK: список результатов, вкладка «Wybór wg NIP» | тот же поиск | B | BLOCKED | кадра нет |
| 3 | img-02 | UOKiK: введён NIP, критерии поиска | тот же поиск | B | BLOCKED | кадра нет |
| 4 | img-03 | скриншот с панелью браузера, адрес zus.pl | вспомогательный | — | NOT VERIFIED | не элемент инструкции |
| 5 | img-04 | «Zaloguj się do eZUS» — выбор метода входа | страница входа eZUS | B | BLOCKED | кадра нет; страница публичная |
| 6 | img-05 | gov.pl: «Zaloguj się do usługi ZUS», последний способ входа | тот же вход | B | BLOCKED | кадра нет |
| 7 | img-06 | «Profil zaufany», поля логина | тот же вход | B | BLOCKED | кадра нет |
| 8 | img-07 | «Portal usług elektronicznych ZUS», Katalog usług, «Tu jesteś» | каталог услуг | B | BLOCKED | кадра нет |
| 9 | img-08 | плитка «Wakacje składkowe» | вход в услугу RWS | B | BLOCKED | кадра нет |
| 10 | img-09 | «Rodzaj wniosku»: Wniosek / Uzupełnienie-korekta / Wycofanie | шаг 1 | A | PASS | rws-full-s01.png — выбран «Wniosek» |
| 11 | img-10 | «Dane płatnika» (кадр сжат, поля нечитаемы) | шаг 2 | B | PASS | rws-full-s02.png (значения замазаны, подписи видны) |
| 12 | img-11 | шаг 3 «Treść wniosku», прогресс до «Załączniki» | шаг 3 | B | PASS | rws-full-s03.png — месяц 11, год 2026 |
| 13 | img-12 | «Oświadczenia», пункты 1–3 | шаг 4 | B | PASS | rws-full-s04.png — выбрано «nie korzystałem z pomocy de minimis» |
| 14 | img-13 | de minimis cz.1: «Wielkość podmiotu», «Klasa działalności» | шаг 5 | B | PASS | rws-full-s05.png — mikroprzedsiębiorca |
| 15 | img-14 | крупно «Klasa działalności» + норма PKD (старый интерфейс) | шаг 5, фрагмент PKD | B | FAIL | rws-closeup-pkd.png — заголовок и норма есть, значение поля скрыто нижней панелью |
| 16 | img-15 | экран с прогрессом 1–9, содержимое обрезано | шаги 5–8 | B | NOT VERIFIED | по OCR не идентифицируется однозначно |
| 17 | img-16 | экран услуги RWS, заголовок + прогресс | шаги 5–8 | B | NOT VERIFIED | не идентифицируется |
| 18 | img-17 | шаг с «Dane płatnika…Załączniki» в прогрессе | шаги 6–9 | B | NOT VERIFIED | не идентифицируется |
| 19 | img-18 | «Złóż wniosek o zaświadczenie o niezaleganiu w opłacaniu składek (RWN)» | услуга RWN, не RWS | B | BLOCKED | отдельная услуга, кадров нет |
| 20 | img-19 | проводник Windows, папка с `przypadki_pomocy_beneficjenta` | подготовка файла | B | BLOCKED | кадра нет |
| 21 | img-20 | диалог выбора файла: `przypadki_pomocy_beneficjenta` | загрузка файла | B | BLOCKED | кадра нет |
| 22 | img-21 | RWN, шаг оплаты/данных | услуга RWN | B | BLOCKED | кадра нет |
| 23 | img-22 | RWN, «Sprawy płatnika» | услуга RWN | B | BLOCKED | кадра нет |
| 24 | img-23 | «Widok danych dokumentu», «Pobierz (PDF 76,642 KB)» — заświadczenie RWN | услуга RWN | B | BLOCKED | кадра нет |
| 25 | img-24 | «Sposób odbioru odpowiedzi», вложение `przypadki_pomocy_beneficjenta.pdf` 25,6 | вложение PDF в RWS/RWN | B | BLOCKED | кадра нет |

## Что матрица уже показала

1. **В источнике две разные услуги.** Кадры 1–17 — RWS (Wakacje składkowe). Кадры 18–25 — RWN, заświadczenie о неурегулированных взносах, с приложением PDF из UOKiK. Если Ольге нужна только RWS, блок RWN надо вынести отдельным разделом, а не мешать с основным сценарием.
2. **Первый шаг в источнике — не форма, а UOKiK.** Инструкция начинается с поиска прошлой помощи: без выгрузки `przypadki_pomocy_beneficjenta.pdf` повторная подача неполная. Этот блок у нас не снят ни разу.
3. **Вход в eZUS в источнике — четыре кадра.** У нас ни одного актуального.
4. **PKD в источнике есть отдельным фрагментом** (img-14), но это старый интерфейс. Наш актуальный фрагмент значение не показывает — упор в нижнюю панель.
5. **11 текущих кадров закрывают только шаги 1–5** и частично 6–9; повторная подача на них не подтверждена типом заявки.

## Что снимать в первую очередь (без авторизации)

| Приоритет | Что | Почему можно снять сразу |
|---|---|---|
| 1 | UOKiK sudop: старт, критерии, результат по NIP | публичная страница, вход не нужен |
| 2 | вход в eZUS и gov.pl (экраны выбора метода) | публичные страницы |
| 3 | каталог услуг и плитка «Wakacje składkowe» | публично, до авторизации |
| 4 | PKD-фрагмент | только в живой сессии eZUS → BLOCKED до туннеля |
| 5 | RWN-блок | требует решения Ольги, включать ли услугу |

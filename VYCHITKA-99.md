# Вычитка инструкции: блок за блоком (п. 99)

Файл: `docs/Instrukcja_RWS_powtorna_podanie_OLGA.docx`. Блоков в теле документа: **75** (пустые абзацы-отбивки не считаются). Проверка машинная, скрипт — `scripts/vychitka_99.py`.

## Что проверено автоматически

Эти проверки выполняет `scripts/vychitka_99.py`; их можно повторить командой `/opt/hermes/venv/bin/python3 scripts/vychitka_99.py` и сравнить вывод.

| Проверка | Как повторяется |
|---|---|
| нет русского текста в польском документе | регексп по всем блокам |
| нет PII: NIP, 11 цифр подряд | регексп по всем блокам |
| нет служебных токенов (PASS, F16, RWN, старое имя файла) | список в скрипте |
| нет правила «ZUS wymaga» без пометки «wymóg z instrukcji Olgi» | регексп |
| ссылки «rozdział N» ведут на существующий заголовок | сверка с множеством заголовков |
| `sha8` и `якорь` у каждого блока | вычисляются из текста блока |

## Что подтверждено исполнителем вручную

Это не проверяется скриптом и извне не подтверждается — только заявлением. Проверяемая часть — диффы, они в истории git.

- четыре находки ниже найдены чтением и исправлены в самом DOCX, не в отчёте;
- остальные блоки прочитаны без замечаний — заявление исполнителя;
- что документ проходит у живого человека (п. 100) — не проверялось.

| # | Тип | sha8 | Якорь | Начало текста | Вердикт |
|---|---|---|---|---|---|
| 1 | абзац | `2dc08589` | текст | Wniosek RWS o zwolnienie z opłacania składek — instrukcja dla płatnika | OK |
| 2 | абзац | `7a7c0b97` | раздел | Dokument opisuje wyłącznie interfejs, który działa 21.10.2026. Kadry pochodzą z sesji na koncie płatnika; dane | OK |
| 3 | абзац | `5d9e7504` | текст | Oznaczenia: zdania z dopiskiem «wymóg z instrukcji Olgi» opisują przebieg, który Olga przekazała 21.10.2026 (n | OK |
| 4 | заголовок | `85dfb9ba` | заголовок | 1. Co trzeba mieć pod ręką | OK |
| 5 | абзац | `ee474a26` | текст | Profil Zaufany albo inna metoda podpisu (e-dowód, podpis kwalifikowany). | OK |
| 6 | абзац | `dd98bd47` | текст | NIP firmy i numer PESEL — system podstawia je sam, ale trzeba sprawdzić. | OK |
| 7 | абзац | `a95dc1ec` | текст | Kod PKD z klasyfikacji PKD 2025, np. 7311Z dla działalności reklamowej. | OK |
| 8 | абзац | `164b953f` | текст | Wysokość przychodu i dochodu za miesiąc, którego dotyczy wniosek. | OK |
| 9 | абзац | `9aa12bb3` | текст | Informacje o pomocy de minimis otrzymanej w ciągu 3 poprzednich lat. | OK |
| 10 | абзац | `99a7bded` | шаг 9 — кадр есть | Plik PDF z «Wyszukiwanie pomocy otrzymanej przez beneficjenta» (SUDOP UOKiK), pobrany pod NIP. Przy wniosku po | OK |
| 11 | абзац | `616eb8c1` | текст | PDF z SUDOP jest obowiązkowy przy wniosku powtarzanym. Inne załączniki — tylko jeśli urząd ich wymaga w tej sp | OK |
| 12 | заголовок | `54507d6c` | заголовок | 1a. Kolejność: najpierw dane z UOKiK, potem wniosek | OK |
| 13 | абзац | `9a0e8acf` | текст | Przy powtarzanym wniosku kolejność ma znaczenie: kwoty pomocy de minimis bierzesz z dokumentu, a nie z pamięci | OK |
| 14 | абзац | `2e07a011` | текст | Wejdź na sudop.uokik.gov.pl i wybierz «Wyszukiwanie pomocy otrzymanej przez beneficjenta». | OK |
| 15 | абзац | `1ad0981d` | текст | Ustaw «Wybór wg NIP», wpisz NIP płatnika. | OK |
| 16 | абзац | `dc4b8a63` | текст | Zaznacz «tylko de minimis» i ustaw «Data udzielenia pomocy» na ostatnie 3 lata. | OK |
| 17 | абзац | `b60a6735` | текст | Wybierz format zapisu wyników «PDF» i kliknij «Wyszukaj według wybranych kryteriów». | OK |
| 18 | абзац | `0f36bfa3` | шаг 4,9 — кадр есть | Pobierz plik z listą pomocy i sumami w euro. Zachowaj go — będzie potrzebny w kroku 4 i kroku 9. | OK |
| 19 | абзац | `94d63916` | текст | Wymóg pobrania i dołączenia tego pliku opisany jest jako «wymóg z instrukcji Olgi». Ekran kreatora sam nie inf | OK |
| 20 | заголовок | `0efaeda0` | заголовок | 2. Wejście do usługi | OK |
| 21 | абзац | `70657b8a` | текст | Zaloguj się do eZUS (PUE ZUS). | OK |
| 22 | абзац | `231988ee` | текст | W menu wybierz «Katalog usług» i wpisz w wyszukiwarce: Wakacje składkowe. | OK |
| 23 | абзац | `03fe15f2` | текст | Otwórz grupę i kliknij «Złóż wniosek o zwolnienie z opłacania składek (RWS)». | OK |
| 24 | абзац | `6b5e032c` | текст | Następnie «Przejdź do usługi» — otwiera się kreator. | OK |
| 26 | абзац | `27317c8d` | текст | Ekran po zalogowaniu: katalog usług w lewym menu | OK |
| 28 | абзац | `833003af` | текст | Katalog usług po wyszukaniu «Wakacje składkowe» | OK |
| 30 | абзац | `bbc04ac9` | текст | Rozwinięta grupa: «Przejdź do usługi» i «Podgląd» | OK |
| 31 | заголовок | `3764aa9e` | заголовок | 3. Kreator ma 11 kroków | OK |
| 32 | абзац | `40e56b11` | шаг 9,10,11 — кадр есть | To jest najważniejsza różnica względem starszych poradników: kreator nie kończy się na kroku 9. Podsumowanie t | OK |
| 33 | таблица 12x2 | `348e635e` | текст | Krok / Nazwa w interfejsie / 1 / Informacje ogólne i rodzaj wniosku / 2 / Dane płatnika / 3 / Treść wniosku —  | OK |
| 34 | заголовок | `0f588415` | заголовок | 4. Krok 1 — rodzaj wniosku | OK |
| 35 | абзац | `3bb181fe` | шаг 1 — кадр есть | W kroku 1 wybierasz jedną z trzech opcji: nowy «Wniosek», «Uzupełnienie/korekta wniosku» albo «Wycofanie wnios | OK |
| 37 | абзац | `5eefc280` | шаг 1 — кадр есть | Krok 1: wybór rodzaju wniosku | OK |
| 38 | заголовок | `f789132b` | заголовок | 4a. Krok 4 — Oświadczenia: wariant z zaświadczeniem | OK |
| 39 | абзац | `d8acee51` | шаг 4 — кадр есть | Krok 4 zawiera wybór, który decyduje o sposobie potwierdzenia pomocy de minimis. W pytaniu 3 są dwie opcje: «n | OK |
| 40 | абзац | `5191d5f6` | текст | Pod nim stoi pytanie «Dla potwierdzenia wielkości otrzymanej pomocy publicznej składam:» z opcjami «oświadczen | OK |
| 41 | абзац | `f8a4cc03` | раздел | W tym scenariuszu zaświadczeniem jest dokument pobrany w rozdziale 1a z SUDOP — tak wynika z opisu Olgi. Kwota | OK |
| 43 | абзац | `16968649` | шаг 4 — кадр есть | Krok 4 «Oświadczenia»: «korzystałem…», a pod nim «oświadczenie» / «zaświadczenie» | OK |
| 44 | абзац | `81fae172` | текст | Ekran nie zawiera zdania, że wybór «oświadczenie» blokuje rozpatrzenie wniosku. To wiedza z instrukcji Olgi, n | OK |
| 45 | заголовок | `382853c9` | заголовок | 5. Jeśli wniosek za ten miesiąc już został złożony | OK |
| 46 | абзац | `223afbf6` | шаг 3 — кадр есть | Przy próbie złożenia drugiego wniosku za ten sam miesiąc kreator zatrzymuje się w kroku 3 i pokazuje komunikat | OK |
| 48 | абзац | `6c265879` | текст | Blokada powtórnego wniosku za ten sam miesiąc | OK |
| 49 | абзац | `11ecd83e` | текст | Droga wyjścia jest jedna z dwóch: korekta złożonego wniosku albo jego wycofanie. | OK |
| 50 | абзац | `4cd1133e` | шаг 1 — кадр есть | W kroku 1 wybierz «Uzupełnienie/korekta wniosku» i kliknij «Dalej». | OK |
| 51 | абзац | `d7a0ef38` | текст | System pokaże tabelę «Wybór wniosku do korekty/uzupełnienia» — z datą, okresem i statusem. | OK |
| 52 | абзац | `49c20c7a` | текст | Kliknij «Koryguj» przy właściwym wierszu. | OK |
| 53 | абзац | `ac901639` | текст | Otworzy się ten sam kreator, ale z danymi już wpisanymi. Poprawiasz tylko to, co trzeba. | OK |
| 55 | абзац | `f304218a` | шаг 1 — кадр есть | Krok 1: wybrana opcja «Uzupełnienie/korekta» | OK |
| 57 | абзац | `0b6348bf` | текст | Tabela wniosków do korekty: okres 11.2026, status «Wysłany» | OK |
| 58 | заголовок | `d6ff074e` | заголовок | 6. Krok 5 — tu jest PKD | OK |
| 59 | абзац | `fdd373c2` | шаг 1,2,3,5 — кадр есть | Pole «Wpisz kod PKD» znajduje się w kroku 5, w sekcji pomocy de minimis, razem z wyborem wielkości podmiotu. N | OK |
| 60 | абзац | `431907cd` | текст | W obserwowanej sesji pole było wypełnione wartością 7311Z, a pod nim widniał opis: «PKD 2025 — Rozporządzenie  | OK |
| 62 | абзац | `fceb7c87` | шаг 5 — кадр есть | Krok 5: wielkość podmiotu i klasa działalności (PKD) | OK |
| 64 | абзац | `36221ba4` | текст | Zbliżenie: pole «Wpisz kod PKD» z wartością 7311Z | OK |
| 65 | заголовок | `27f9d8d7` | заголовок | 6a. Kroki 6–8: pozostałe części pomocy de minimis | OK |
| 66 | абзац | `cd08c964` | шаг 4,6,7 — кадров нет | W naszej sesji te trzy kroki nie zostały nagrane, dlatego nie opisujemy ich treści. W pliku Olgi są pokazane n | OK |
| 67 | заголовок | `93d21b88` | заголовок | 7. Kroki 9–11: załączniki, podsumowanie, podpis | OK |
| 68 | абзац | `57d1289f` | шаг 9 — кадр есть | Ważne: przy wniosku powtarzanym dołączasz plik pobrany w rozdziale 1a z SUDOP. Bez tego pliku wniosek nie zost | OK |
| 69 | абзац | `ad229c4c` | шаг 9 — кадр есть | Krok 9 to ekran «Załączniki». Na ekranie widnieje lista formatów (.doc, .docx, .pdf, .jpg, .png, .xlsx, .zip i | OK |
| 70 | абзац | `ce7128e5` | шаг 9,10,11 — кадр есть | Krok 9 «Załączniki» — w powtarzanym wniosku dodajesz tu PDF z SUDOP (rozdział 1a). Inne pliki dodajesz tylko w | OK |
| 72 | абзац | `321fdd57` | шаг 9 — кадр есть | Krok 9: załączniki | OK |
| 74 | абзац | `caedeecb` | шаг 10 — кадр есть | Krok 10: podsumowanie wniosku | OK |
| 76 | абзац | `1e08d9fc` | шаг 11 — кадр есть | Krok 11: okno wyboru metody podpisu | OK |
| 77 | заголовок | `09aa9e40` | заголовок | 8. Jeśli ekran nie zgadza się z instrukcją | OK |
| 78 | абзац | `ed05e46b` | текст | Sprawdź adres: katalog usług to /platnika/katalog-uslug, kreator — /rws/.... | OK |
| 79 | абзац | `34235eb6` | текст | Wyczyść pamięć podręczną przeglądarki i wejdź ponownie przez «Katalog usług». | OK |
| 80 | абзац | `adedfdf8` | текст | Nie korzystaj z zakładek zapisanych pół roku temu — adresy kreatora się zmieniają. | OK |
| 81 | абзац | `ab1033c0` | раздел | Jeśli komunikat jest inny niż w rozdziale 5, zrób zrzut ekranu i przerwij — nie klikaj «Dalej» na oślep. | OK |
| 82 | заголовок | `a8c3fb23` | заголовок | 9. Źródła | OK |
| 83 | абзац | `87ddd488` | текст | ZUS — Wakacje składkowe: https://www.zus.pl/wakacje-skladkowe | OK |
| 84 | абзац | `43cbe170` | текст | eZUS / PUE: https://www.zus.pl/ezus | OK |
| 85 | абзац | `00da7ba7` | текст | PKD 2025: Rozporządzenie Rady Ministrów z 18.12.2024, Dz.U. 2024 poz. 1936 | OK |
| 86 | абзац | `06107d00` | текст | SUDOP UOKiK (pomoc de minimis): https://sudop.uokik.gov.pl | OK |
| 87 | абзац | `14da038d` | текст | Instrukcja Olgi, przekazana 21.10.2026 (nagranie głosowe i zrzuty ekranu; streszczenie w Issue #1): kolejność  | OK |
| 88 | абзац | `26dedaff` | текст | Dokument przygotowany 21.10.2026 na podstawie sesji w eZUS. Wartości PKD i status wniosku potwierdzone wyłączn | OK |

## Сводка

- блоков проверено: 75
- с замечаниями: 0
- блоков, которые держатся на шагах 6–8 без кадров: 2 (блоки 66, 67)

Замечаний нет.

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

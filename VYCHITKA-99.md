# Вычитка инструкции: блок за блоком (п. 99)

Файл: `docs/Instrukcja_RWS_powtorna_podanie_OLGA.docx`. Блоков в теле документа: **73** (пустые абзацы-отбивки не считаются). Проверка машинная, скрипт — `scripts/vychitka_99.py`.

Инварианты: нет русского текста; нет PII (NIP/PESEL); нет служебных токенов (PASS, F16, RWN, имя файла из старого документа); нет правила «ZUS wymaga» без пометки «wymóg z instrukcji Olgi»; все ссылки «rozdział N» ведут на существующий заголовок.

| # | Тип | Начало текста | Вердикт |
|---|---|---|---|
| 1 | абзац | Wniosek RWS o zwolnienie z opłacania składek — instrukcja dla płatnika | OK |
| 2 | абзац | Dokument opisuje wyłącznie interfejs, który działa 21.10.2026. Kadry pochodzą z sesji na k | OK |
| 3 | абзац | Oznaczenia: zdania z dopiskiem «wymóg z instrukcji Olgi» opisują przebieg, który Olga prze | OK |
| 4 | заголовок | 1. Co trzeba mieć pod ręką | OK |
| 5 | абзац | Profil Zaufany albo inna metoda podpisu (e-dowód, podpis kwalifikowany). | OK |
| 6 | абзац | NIP firmy i numer PESEL — system podstawia je sam, ale trzeba sprawdzić. | OK |
| 7 | абзац | Kod PKD z klasyfikacji PKD 2025, np. 7311Z dla działalności reklamowej. | OK |
| 8 | абзац | Wysokość przychodu i dochodu za miesiąc, którego dotyczy wniosek. | OK |
| 9 | абзац | Informacje o pomocy de minimis otrzymanej w ciągu 3 poprzednich lat. | OK |
| 10 | абзац | Plik PDF z «Wyszukiwanie pomocy otrzymanej przez beneficjenta» (SUDOP UOKiK), pobrany pod  | OK |
| 11 | абзац | PDF z SUDOP jest obowiązkowy przy wniosku powtarzanym. Inne załączniki — tylko jeśli urząd | OK |
| 12 | заголовок | 1a. Kolejność: najpierw dane z UOKiK, potem wniosek | OK |
| 13 | абзац | Przy powtarzanym wniosku kolejność ma znaczenie: kwoty pomocy de minimis bierzesz z dokume | OK |
| 14 | абзац | Wejdź na sudop.uokik.gov.pl i wybierz «Wyszukiwanie pomocy otrzymanej przez beneficjenta». | OK |
| 15 | абзац | Ustaw «Wybór wg NIP», wpisz NIP płatnika. | OK |
| 16 | абзац | Zaznacz «tylko de minimis» i ustaw «Data udzielenia pomocy» na ostatnie 3 lata. | OK |
| 17 | абзац | Wybierz format zapisu wyników «PDF» i kliknij «Wyszukaj według wybranych kryteriów». | OK |
| 18 | абзац | Pobierz plik z listą pomocy i sumami w euro. Zachowaj go — będzie potrzebny w kroku 4 i kr | OK |
| 19 | абзац | Wymóg pobrania i dołączenia tego pliku opisany jest jako «wymóg z instrukcji Olgi». Ekran  | OK |
| 20 | заголовок | 2. Wejście do usługi | OK |
| 21 | абзац | Zaloguj się do eZUS (PUE ZUS). | OK |
| 22 | абзац | W menu wybierz «Katalog usług» i wpisz w wyszukiwarce: Wakacje składkowe. | OK |
| 23 | абзац | Otwórz grupę i kliknij «Złóż wniosek o zwolnienie z opłacania składek (RWS)». | OK |
| 24 | абзац | Następnie «Przejdź do usługi» — otwiera się kreator. | OK |
| 26 | абзац | Ekran po zalogowaniu: katalog usług w lewym menu | OK |
| 28 | абзац | Katalog usług po wyszukaniu «Wakacje składkowe» | OK |
| 30 | абзац | Rozwinięta grupa: «Przejdź do usługi» i «Podgląd» | OK |
| 31 | заголовок | 3. Kreator ma 11 kroków | OK |
| 32 | абзац | To jest najważniejsza różnica względem starszych poradników: kreator nie kończy się na kro | OK |
| 33 | таблица 12x2 | Krok / Nazwa w interfejsie / 1 / Informacje ogólne i rodzaj wniosku / 2 / Dane płatnika /  | OK |
| 34 | заголовок | 4. Krok 1 — rodzaj wniosku | OK |
| 35 | абзац | W kroku 1 wybierasz jedną z trzech opcji: nowy «Wniosek», «Uzupełnienie/korekta wniosku» a | OK |
| 37 | абзац | Krok 1: wybór rodzaju wniosku | OK |
| 38 | заголовок | 4a. Krok 4 — Oświadczenia: wariant z zaświadczeniem | OK |
| 39 | абзац | Krok 4 zawiera wybór, który decyduje o sposobie potwierdzenia pomocy de minimis. W pytaniu | OK |
| 40 | абзац | Pod nim stoi pytanie «Dla potwierdzenia wielkości otrzymanej pomocy publicznej składam:» z | OK |
| 41 | абзац | W tym scenariuszu zaświadczeniem jest dokument pobrany w rozdziale 1a z SUDOP — tak wynika | OK |
| 43 | абзац | Krok 4 «Oświadczenia»: «korzystałem…», a pod nim «oświadczenie» / «zaświadczenie» | OK |
| 44 | абзац | Ekran nie zawiera zdania, że wybór «oświadczenie» blokuje rozpatrzenie wniosku. To wiedza  | OK |
| 45 | заголовок | 5. Jeśli wniosek za ten miesiąc już został złożony | OK |
| 46 | абзац | Przy próbie złożenia drugiego wniosku za ten sam miesiąc kreator zatrzymuje się w kroku 3  | OK |
| 48 | абзац | Blokada powtórnego wniosku za ten sam miesiąc | OK |
| 49 | абзац | Droga wyjścia jest jedna z dwóch: korekta złożonego wniosku albo jego wycofanie. | OK |
| 50 | абзац | W kroku 1 wybierz «Uzupełnienie/korekta wniosku» i kliknij «Dalej». | OK |
| 51 | абзац | System pokaże tabelę «Wybór wniosku do korekty/uzupełnienia» — z datą, okresem i statusem. | OK |
| 52 | абзац | Kliknij «Koryguj» przy właściwym wierszu. | OK |
| 53 | абзац | Otworzy się ten sam kreator, ale z danymi już wpisanymi. Poprawiasz tylko to, co trzeba. | OK |
| 55 | абзац | Krok 1: wybrana opcja «Uzupełnienie/korekta» | OK |
| 57 | абзац | Tabela wniosków do korekty: okres 11.2026, status «Wysłany» | OK |
| 58 | заголовок | 6. Krok 5 — tu jest PKD | OK |
| 59 | абзац | Pole «Wpisz kod PKD» znajduje się w kroku 5, w sekcji pomocy de minimis, razem z wyborem w | OK |
| 60 | абзац | W obserwowanej sesji pole było wypełnione wartością 7311Z, a pod nim widniał opis: «PKD 20 | OK |
| 62 | абзац | Krok 5: wielkość podmiotu i klasa działalności (PKD) | OK |
| 64 | абзац | Zbliżenie: pole «Wpisz kod PKD» z wartością 7311Z | OK |
| 65 | заголовок | 7. Kroki 9–11: załączniki, podsumowanie, podpis | OK |
| 66 | абзац | Ważne: przy wniosku powtarzanym dołączasz plik pobrany w rozdziale 1a z SUDOP. Bez tego pl | OK |
| 67 | абзац | Krok 9 to ekran «Załączniki». Na ekranie widnieje lista formatów (.doc, .docx, .pdf, .jpg, | OK |
| 68 | абзац | Krok 9 «Załączniki» — w powtarzanym wniosku dodajesz tu PDF z SUDOP (rozdział 1a). Inne pl | OK |
| 70 | абзац | Krok 9: załączniki | OK |
| 72 | абзац | Krok 10: podsumowanie wniosku | OK |
| 74 | абзац | Krok 11: okno wyboru metody podpisu | OK |
| 75 | заголовок | 8. Jeśli ekran nie zgadza się z instrukcją | OK |
| 76 | абзац | Sprawdź adres: katalog usług to /platnika/katalog-uslug, kreator — /rws/.... | OK |
| 77 | абзац | Wyczyść pamięć podręczną przeglądarki i wejdź ponownie przez «Katalog usług». | OK |
| 78 | абзац | Nie korzystaj z zakładek zapisanych pół roku temu — adresy kreatora się zmieniają. | OK |
| 79 | абзац | Jeśli komunikat jest inny niż w rozdziale 5, zrób zrzut ekranu i przerwij — nie klikaj «Da | OK |
| 80 | заголовок | 9. Źródła | OK |
| 81 | абзац | ZUS — Wakacje składkowe: https://www.zus.pl/wakacje-skladkowe | OK |
| 82 | абзац | eZUS / PUE: https://www.zus.pl/ezus | OK |
| 83 | абзац | PKD 2025: Rozporządzenie Rady Ministrów z 18.12.2024, Dz.U. 2024 poz. 1936 | OK |
| 84 | абзац | SUDOP UOKiK (pomoc de minimis): https://sudop.uokik.gov.pl | OK |
| 85 | абзац | Instrukcja Olgi, przekazana 21.10.2026 (nagranie głosowe i zrzuty ekranu; streszczenie w I | OK |
| 86 | абзац | Dokument przygotowany 21.10.2026 na podstawie sesji w eZUS. Wartości PKD i status wniosku  | OK |

## Сводка

- блоков проверено: 73
- с замечаниями: 0

Замечаний нет.

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

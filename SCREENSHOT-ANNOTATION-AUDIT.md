# Сопоставление скриншотов Ольги и живой сессии

Метод: ORB-гомография кадров DOCX ↔ живые кадры; перенос красных пикселей маской. Уверенность — доля inlier-точек.

| DOCX (стр., рис.) | Действие Ольги | Целевой кадр | Элемент | Стрелка | Подпись (ru) | Польский текст | Уверенность | Статус |
|---|---|---|---|---|---|---|---|---|
| 2, рис. 1 | открыть SUDOP | sudop-1-0 | поле NIP | слева, на поле | введите NIP | NIP | высокая (472) | CONFIRMED |
| 3, рис. 2 | подставить название | sudop-1-1 | Pobierz nazwę | слева | нажмите | Pobierz nazwę | высокая | CONFIRMED |
| 3, рис. 3 | отметить только de minimis | sudop-1-1 | чекбокс | слева | только de minimis | tylko de minimis | высокая | CONFIRMED |
| 4, рис. 4 | выбрать PDF | sudop-2-0 | Formacie: PDF | слева | формат PDF | PDF | высокая | CONFIRMED |
| 5, рис. 5 | нажать поиск | sudop-2-0 | Wyszukaj… | слева | искать | Wyszukaj według wybranych kryteriów | высокая | CONFIRMED |
| 6, рис. 6 | вход на zus.pl | login-ezus-0 | Zaloguj do PUE/eZUS | перенесена | войти | Zaloguj do PUE/eZUS | высокая (231) | CONFIRMED |
| 6, рис. 7 | login.gov.pl | login-ezus-1 | кнопка login.gov.pl | перенесена | вход через login.gov.pl | login.gov.pl | высокая | CONFIRMED |
| 7, рис. 8 | каталог услуг | login-ezus-0 (низ) | Wakacje składkowe | перенесена | выберите услугу | Wakacje składkowe | средняя | CONFIRMED |
| 8, рис. 9 | Rodzaj wniosku = RWS | wniosek-0 | Rodzaj wniosku | перенесена | выберите RWS | Rodzaj wniosku | высокая | CONFIRMED |
| 9, рис. 10 | Dalej | wniosek-1 | Dalej | перенесена | далее | Dalej | высокая | CONFIRMED |
| 10, рис. 11 | проверить NIP | platnik-0 | Numer telefonu | нарисована | телефон можно не заполнять | Numer telefonu (opcjonalnie) | средняя | AMBIGUOUS |
| 11, рис. 12 | месяц | miesiac-0 | Miesiąc: 11 | перенесена | проверьте месяц | Miesiąc | высокая | CONFIRMED |
| 12, рис. 13 | Oświadczenia п.1 | oswiadczenia-0 | радиокнопка 1 | нарисована | отметьте | Oświadczam, że | средняя | AMBIGUOUS |
| 13, рис. 14 | TAK в п. a | dm2-0 | радиокнопка TAK | нарисована | выберите TAK | TAK | средняя | AMBIGUOUS |
| 14, рис. 15 | TAK в п. a | dm3-0 | радиокнопка TAK | нарисована | выберите TAK | TAK | средняя | AMBIGUOUS |
| 15, рис. 16 | TAK в п. a | dm4-0 | радиокнопка TAK | нарисована | выберите TAK | TAK | средняя | AMBIGUOUS |
| 16, рис. 17 | загрузка файла | zalaczniki-0 | пунктирная зона | нарисована | нажмите зону | Wybierz plik | средняя | AMBIGUOUS |
| 17, рис. 18 | Przejdź / Podgląd | podsumowanie-0 | Podgląd i wyślij | нарисована | отправьте | Podgląd i wyślij | средняя | AMBIGUOUS |
| 18, рис. 19 | подпись | podpis (без кадра) | — | — | подпишите | Podpisz | — | NO MATCH |
| 19, рис. 20 | UPO | — | — | — | — | — | — | NO MATCH |
| 20, рис. 21 | диалог выбора файла | zalaczniki-1 | окно ОС | нет | — | — | — | NOT APPLICABLE |
| 21, рис. 22 | фрагмент загрузки | zalaczniki-1 | фрагмент | нет | — | — | — | NOT APPLICABLE |
| 22, рис. 23 | пустая форма | — | — | — | — | — | — | NO MATCH |

Итого: 23 изображения в DOCX; CONFIRMED 12, AMBIGUOUS 6, NO MATCH 3, NOT APPLICABLE 2.
Нанесено стрелок: 19 из 19 изображений на сайте; из них 10 перенесены гомографией, 7 нарисованы вручную, 2 без цели.

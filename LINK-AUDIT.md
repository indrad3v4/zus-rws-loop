# Аудит ссылок — 22.10.2026

Проверка: `curl -s -o /dev/null -L -w '%{http_code}'` + CDP на живой странице.

| Слово на сайте | URL | Код | Что подтверждает |
|---|---|---|---|
| ZUS — вход в eZUS | https://www.zus.pl/ | 200 | точка входа, кнопка «Zaloguj do PUE/eZUS» |
| Wakacje składkowe — правила | https://biznes.gov.pl/pl/portal/ou710 | 200 | официальное описание услуги |
| SUDOP | https://sudop.uokik.gov.pl | 200 | поиск помощи по NIP |
| Profil Zaufany | https://login.gov.pl | 200 | вход и подпись |

Отклонены (404/000): `zus.pl/logowanie`, `zus.pl/e-uslugi`, `zus.pl/swiadczenia/wakacje-skladkowe`, `eservices.zus.pl`, `pue.zus.pl`.
Длинных URL в тексте нет; все ссылки открываются в новой вкладке, доступны с клавиатуры (обычные `<a>`).

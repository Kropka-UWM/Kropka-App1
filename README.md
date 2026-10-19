![django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![drf](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![js](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![vue](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D)

# Aplikacja nr 1 [Projekt zespołowy UWM]
### Skład zespołu:
* Mateusz Szczygłów
* Grzegorz Choczaj
* Patryk Szczepański
* Dawid Zagórski
* Krzysztof Wysocki
* Przemysław Samsel

# Czego wymaga backend?
Backend używa Django 6.1.2. Zalecany Python to 3.15 (zapisany w `.python-version`).
GitHub Actions sprawdza Python 3.12, 3.13, 3.14 i 3.15.

Chat obsługuje Channels 4 z serwerem ASGI Daphne. Do komunikacji między procesami potrzebny
jest Redis dostępny domyślnie pod `127.0.0.1:6379`.

Generowanie PDF przez WeasyPrint wymaga bibliotek systemowych Pango. Na Ubuntu:

```sh
sudo apt-get install libpango-1.0-0 libpangoft2-1.0-0
```

Na macOS z Homebrew: `brew install pango`. Jeżeli biblioteki nie są wykrywane automatycznie,
ustaw `DYLD_FALLBACK_LIBRARY_PATH="$(brew --prefix)/lib"`.

# Czego wymaga frontend?
Node.js 24.15 lub nowszy z linii 24 LTS albo Node.js 26. Frontend używa Vue 3.5,
Vite 8, Vitest 5 i ESLint 10. Obie linie Node.js są sprawdzane w CI.

TypeScript pozostaje w najnowszej zgodnej linii 6.0 (6.0.3), ponieważ `typescript-eslint`
nie obsługuje jeszcze TypeScript 7. `vuedraggable` używa linii 4 dla Vue 3;
pakiet oznaczony w npm jako `latest` z linii 2 jest przeznaczony dla Vue 2.

# Jak stworzyć konto superuser, czyli administratora w django?
Konto superusera tworzymy za pomocą komendy `python manage.py createsuperuser`, 
a następnie wypełniamy informacje w interaktywnym kreatorze w konsoli/terminalu.

Dodatkowo warto dodać, że panel administratora do całej bazy znajduje się pod adresem `<tu_domena>/admin/`

# Jak uruchomić projekt?
Utwórz środowisko i zainstaluj zależności z poziomu głównego katalogu:

```sh
python3.15 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements_dev.txt
mkdir -p backend/logs
python manage.py migrate
python manage.py runserver
```

Domyślnie jest tworzona baza SQLite. Możemy skopiować `backend/project/settings_local.example`
jako `backend/project/settings_local.py` -
a następnie zmodyfikować jego zawartość tak aby ten plik zawierał konfigurację np. do połączenia z MySQL albo PostgreSQL.

Same nazwy backendów które trzeba umieścić są opisane w dokumentacji na stronie django.

Uruchomienie frontu:

```
cd frontend
npm ci
npm run serve
```

Frontend jest dostępny pod `http://localhost:8080`.

Sprawdzenie projektu przed wysłaniem zmian (backend nie wymaga Redisa w testach):

```sh
python -m pip check
flake8 .
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
cd frontend
npm run lint
npm run test:unit
npm run build
```

Po aktualizacji uruchom `python manage.py migrate`, aby zastosować również migracje dodatków
allauth i push-notifications. Przed migracją istniejącej instalacji wykonaj kopię bazy danych.

# Endpointy [backend]:
* **Autentykacja**:
  * /register/
  * /login/
  * /logout/
  * /password-reset/
  * /get_account_info/
  * /password/change/
* Reszta:
  * /group_students/
  * /list_students/
  * /list_companies/
  * /assign_student/
  * /get_conversations/
  * /get_messages/
  * /get_messages/<conversation_id>/
  * /get_site_settings/

# Widoki [Demo]:
* /demo404/
* /demo500/
* /chat-demo/
* /chat-demo/<chat_name>/
* /push-demo/

# Komendy (python manage.py ...):
* generate_companies [ilosc]
* generate_leaders [ilosc]
* generate_teams <company_id> [ilosc]
* generate_user_companies [ilosc]
* generate_students [ilosc]

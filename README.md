# Aplikacja nr 1 [Projekt zespołowy UWM]
### Skład zespołu:
* Mateusz Szczygłów
* Grzegorz Choczaj
* Patryk Szczepański
* Dawid Zagórski
* Krzysztof Wysocki
* Przemysław Samsel

# Czego wymaga backend?
Backend powinien być obsługiwany od pythona 3.6 w górę (zalecana najbardziej wersja prze ze mnie to 3.8)

Dodatkowo wymaga obsługę ASGI do funkcjonalności chatu.

# Czego wymaga frontend?
Wystarczy zainstalować aktualną, stabilną wersje node.js - na tą chwile 16.15.1

# Jak stworzyć konto superuser, czyli administratora w django?
Konto superusera tworzymy za pomocą komendy `python manage.py createsuperuser`, 
a następnie wypełniamy informacje w interaktywnym kreatorze w konsoli/terminalu.

Dodatkowo warto dodać, że panel administratora do całej bazy znajduje się pod adresem `<tu_domena>/admin/`

# Fix pod python 3.10:
```
pip install hyperframe==6.0.1
pip install h2==4.1.0
```

# Jak uruchomić projekt?
Musimy najpierw utworzyć katalog logs w katalogu backend.
Jeżeli chcemy uruchomić projekt, wystarczy iż z poziomu głównego katalogu odpalimy komendę:
```
python manage.py migrate
python manage.py runserver
```

Domyślnie jest tworzona baza danych "plikowa" (sqlite3) ale możemy skopiować settings_local.example jako settings_local.py -
a następnie zmodyfikować jego zawartość tak aby ten plik zawierał konfigurację np. do połączenia z MySQL albo PostgreSQL.

Same nazwy backendów które trzeba umieścić są opisane w dokumentacji na stronie django.

Uruchomienie frontu:

```
cd frontend
npm install
npm run serve
```

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
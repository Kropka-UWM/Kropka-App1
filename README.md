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

# Jak stworzyć konto superuser, czyli administratora w django?
Konto superusera tworzymy za pomocą komendy `python manage.py createsuperuser`, 
a następnie wypełniamy informacje w interaktywnym kreatorze w konsoli/terminalu.

Dodatkowo warto dodać, że panel administratora do całej bazy znajduje się pod adresem `<tu_domena>/admin/`

# Jak uruchomić projekt?
Jeżeli chcemy uruchomić projekt, wystarczy iż z poziomu głównego katalogu odpalimy komendę:
```
python manage.py migrate
python manage.py runserver
```

Domyślnie jest tworzona baza danych "plikowa" (sqlite3) ale możemy skopiować settings_local.example jako settings_local.py -
a następnie zmodyfikować jego zawartość tak aby ten plik zawierał konfigurację np. do połączenia z MySQL albo PostgreSQL.

Same nazwy backendów które trzeba umieścić są opisane w dokumentacji na stronie django.

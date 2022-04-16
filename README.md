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

# Jak uruchomić projekt?
Jeżeli chcemy uruchomić projekt, wystarczy iż z poziomu głównego katalogu odpalimy komendę:
```
python manage.py migrate
python manage.py runserver
```

Domyślnie jest tworzona baza danych "plikowa" (sqlite3) ale możemy skopiować settings_local.example jako settings_local.py -
a następnie zmodyfikować jego zawartość tak aby ten plik zawierał konfigurację np. do połączenia z MySQL albo PostgreSQL.

Same nazwy backendów które trzeba umieścić są opisane w dokumentacji na stronie django.

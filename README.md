# allewatcher

Allewatcher to aplikacja automatycznie wyszukująca aukcje w serwisie allegro na podstawie podanych przez użytkownika kryteriów wyszukiwania w postaci frazy wyszukiwania oraz jednej spośród kategorii głównych serwisu. 

Po uruchomieniu pliku dbase_operations.py przy pomocy API allegro zapisywana do bazy danych jest lista kategorii dzięki czemu jest ona zawsze aktualna. Moduł ten jak i search.py odpowiedzialny za właściwe wyszukiwanie powinien być zapisany w zadaniu Cron. Wynikiem search.py jest przesłanie do użytkownika na podany przez Niego adres email wyników wyszukiwania.

Wyszukiwanie jest ustawiane przez użytkownika za pomocą strony internetowej stworzonej w django, która jest integralną częścią aplikacji oraz aktywowane przez potwierdzenie wysłane na podany przez użytkownika adres email w ciągu 48 godzin, po upływie których zostnie ono usunięte wraz z kolejnym uruchomieniem dbase_operations.py. Każde aktywne wyszukiwanie pozwala na otrzymywanie przez użytkownika wiadomości z wynikami wyszukiwania przez okres 7 dni. Po tym czasie zostaje ono usunięte wraz z kolejnym uruchomieniem dbase_operations.py.

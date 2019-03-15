# Drodzy!
jak poprzednio, zgodnie z obietnicą egzamin przykładowy, mający pomóc Wam przygotowaniu się do egzaminu.
Mam nadzieję, że będzie on pomocny w powtarzaniu materiału!
Nie traktujcie go jednak jako wyznacznika zakresu, a jedynie przykład czego możecie się spodziewać.


----------------------------------------------------------------------------------------

# Programowanie obiektowe i bazy danych &ndash; egzamin.

Przed przystąpieniem do rozwiązywania zadań przeczytaj poniższe wskazówki

## Jak zacząć?

1. Stwórz [*fork*](https://guides.github.com/activities/forking/) repozytorium z zadaniami.
2. Sklonuj repozytorium na swój komputer. Użyj do tego komendy `git clone adres_repozytorium`
Adres repozytorium możesz znaleźć na stronie repozytorium po naciśnięciu w guzik "Clone or download".
3. Rozwiąż zadania i skomituj zmiany do swojego repozytorium. Użyj do tego komend `git add nazwa_pliku`.
Jeżeli chcesz dodać wszystkie zmienione pliki użyj `git add .`
Pamiętaj że kropka na końcu jest ważna!
Następnie skommituj zmiany komendą `git commit -m "nazwa_commita"`
4. Wypchnij zmiany do swojego repozytorium na GitHubie.  Użyj do tego komendy `git push origin master`
5. Stwórz [*pull request*](https://help.github.com/articles/creating-a-pull-request) do oryginalnego repozytorium, gdy skończysz wszystkie zadania.

#### Pamiętaj, że pull request musi być stworzony, aby wykładowca dostał Twoje odpowiedzi.

* podczas egzaminu **możesz** korzystać z notatek, kodu napisanego wcześniej, internetu i prezentacji,
* zabroniona jest jakakolwiek komunikacja z innymi kursantami oraz osobami na zewnątrz.

**Powodzenia!**

----------------------------------------------------------------------------------------

## Pytania otwarte
Odpowiedzi wpisz w pliku **answers.txt**.

----------------------------------------------------------------------------------------

## Pytania teoretyczne
### Pytanie 1.
(1,5 pkt) Dlaczego warto przechowywać dane w bazie danych?

### Pytanie 2.
(2 pkt) Jakie są zalety programowania obektowego? W jaki sposób się je osiąga?

## Zadania praktyczne
Kod wpisz w odpowiednim pliku, zgodnie z poleceniem zadania. Utwórz bazę danych exam2, tam rozwiązuj wszystkie zadania.

### Zadanie 1.
(4,5 pkt) W bazie danych chcemy mieć następujące tabele(notatnik pewnego *privat bankiera*):
```
* Contacts: id : autonumerowany (klucz główny), name : varchar(60), email : varchar(60), company : varchar(60)
* Addresses: id : autonumerowany (klucz główny), street : varchar(40), city: varchar(40), house_number: decimal(4), description : text
* Todos: id : autonumerowany (klucz główny), prio: int, description: text
* Notes: id : autonumerowany (klucz główny), user_id: int, note_text : text
```
Zajrzyj do pliku exercise_1.py, znajdziesz tam zdefiniowane zmienne: query_1, query_2 ... query_9. W zmiennych umieść następujące zapytania SQL:

* sql_1: Tworzące tabelę `Contacts` (email ma być unikatowy).
* sql_2: Tworzące tabelę `Notes` (pamiętaj o relacji jeden do wielu z tabelą Contacts).
* sql_3: Tworzące tabelę `Address`.
* sql_4: Tworzące tabelę `Todos`.
* sql_5: Stworzenie relacji wiele do wielu między tabelami `Contacts` a `Todos` (tabela ma się nazywać `ContactsTodos`, a pola relacji `contact_id` i `todo_id`).
* sql_6: Wybranie wszystkich addresses z ulicy `Polna`.
* sql_7: Włożenie do tabeli `Todos` nowego adresu o opisie "przykładowy opis" i prio 10.
* sql_8: Usuniecie kontaktu o id `7`.
* sql_9: Wybranie wszystkich `kontaktów` z tabeli `Contacts`, którzy mają przypisaną jakąś notatkę w tabeli Notes.

Za każde zapytanie przysługuje pół punktu.

### Zadania 2.
(3 pkt) Napisz funkcję notes(id), która zwróci wszystkie notatki dla kontaktu o identyfikatorze przekazanym jako parametr funkcji. Pamiętaj o poprawnym połączeniu do bazy danych i jego zamknięciu. Następnie używając Flaska, utwórz stronię pod adresem /show_note/{nid} wyświetlającą zadaną notatkę.

### Zadanie 3.
(4 pkt) Używając Flaska, napisz stronę udostępnioną pod adresem /add_address, która spełni następujące założenia:
1. Po wejściu metodą GET wyświetli pusty formularz, który będzie zawierał następujące pola:
    *    street,
    *    city,
    *    house_number,
    *    description
    Pamiętaj: nazwij pola dokładnie tak, jak w poleceniu (ustaw odpowiednio atrybut name taga <input>)

2. Po wejściu metodą POST:
    *    zweryfikuje poprawność danych(długość napisów powinna wynosić minimum 3 znaki, numer domu powinien być liczbą naturalną, większą od zera)
    *    zapisze te dane do bazy danych do odpowiedniej tabeli i wyświetli komunikat "Dodano",
    *    jeśli którakolwiek dana będzie błędna, zamiast zapisywania do bazy, wyświetli na stronie komunikat "Błędne dane".

Pamiętaj o poprawnym połączeniu do bazy danych i jego zamknięciu.

### Zadanie 4
(5 pkt) Napisz program w Pythonie klasy TrustedCustomer. Klasa ma spełniać następujące właściwości:
    * Dziedziczyć po klasie Customer (zajrzyj do modułu exam) oraz mieć dodatkowy atrybut: discount_value.
    * Mieć konstruktor, który przyjmuje następujące dane: `nazwa`, `mail`, `wartość zniżki`. Nazwa i mail mają być przekazywane do konstruktora klasy nadrzędnej. Konstruktor ma sprawdzać, czy podana zniżka jest poprawna. Jeżeli jest – to go nastawiać, jeżeli nie – to wartość ma być ustawiona na 0.0.
    * Mieć prywatną metodę check_discount(value) – zniżka poprawna jeśli jest z przedziału <0.03;0.25>. Funkcja ma zwracać wartość logiczną.
    * Mieć publiczną metodę use_discount() – ciało metody może zostać puste (lub zwrócić wartość None).
    * Mieć publiczną funkcję set_discount_value(new_discount_value) i get_discount_value(). Funkcja set ma nastawiać zmienną discount_value (jeżeli podana nowa wartość spełnia założenia), a funkcja get – ją zwracać.
    * Naspisać publiczną funkcję get_total_price() w sposób uwzględniający zniżkę

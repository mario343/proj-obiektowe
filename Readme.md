# Projektowanie obiektowe

**Zadanie 1** Pascal

Proszę napisać program w Pascalu, który zawiera dwie procedury, jedna generuje listę 50 losowych liczb od 0 do 100. Druga procedura sortuje liczbę za pomocą sortowania bąbelkowego.

:white_check_mark: 3.0 Procedura do generowania 50 losowych liczb od 0 do 100 [Link do commita](https://github.com/mario343/proj-obiektowe/commit/2b6c3946b9b4f351fb27b756c8c27e9c7c9a0d39)

:white_check_mark: 3.5 Procedura do sortowania liczb [Link do commita](https://github.com/mario343/proj-obiektowe/commit/2b6c3946b9b4f351fb27b756c8c27e9c7c9a0d39)

:white_check_mark: 4.0 Dodanie parametrów do procedury losującej określającymi zakres
losowania: od, do, ile [Link do commita](https://github.com/mario343/proj-obiektowe/commit/2b6c3946b9b4f351fb27b756c8c27e9c7c9a0d39)

:x: 4.5 5 testów jednostkowych testujące procedury

:x: 5.0 Skrypt w bashu do uruchamiania aplikacji w Pascalu via docker

Kod: 01-pascal

[DEMO](https://github.com/mario343/proj-obiektowe/blob/main/demos/zadanie1.gif)

**Zadanie 2** PHP

Należy stworzyć aplikację webową na bazie frameworka Symfony na
obrazie kprzystalski/projobj-php:latest. Baza danych dowolna, sugeruję
SQLite.

:white_check_mark: 3.0 Należy stworzyć jeden model z kontrolerem z produktami, zgodnie z CRUD [Link do commita](https://github.com/mario343/proj-obiektowe/commit/b8117c51a0443eccce869f306bfbcb9710cf2716)

:x: 3.5 Należy stworzyć skrypty do testów endpointów via curl

:x: 4.0 Należy stworzyć dwa dodatkowe kontrolery wraz z modelami

:x: 4.5 Należy stworzyć widoki do wszystkich kontrolerów

:x: 5.0 Stworzenie panelu administracyjnego z mockowanym logowaniem

Kod: 02-php

[DEMO](https://github.com/mario343/proj-obiektowe/blob/main/demos/zadanie2.gif)

**Zadanie 3** Springboot - Kotlin

Proszę stworzyć prosty serwis do autoryzacji, który zasymuluje autoryzację użytkownika za pomocą przesłanej nazwy użytkownika oraz
hasła. Serwis powinien zostać wstrzyknięty do kontrolera za pomocą anotacji @Autowired. Aplikacja ma oczywiście zawierać jeden kontroler
i powinna zostać napisana w języku Kotlin. Oparta powinna zostać na frameworku Spring Boot, podobnie jak na zajęciach. Serwis do
autoryzacji powinien być singletonem.

:white_check_mark: 3.0 Należy stworzyć jeden kontroler wraz z danymi wyświetlanymi z
listy na endpoint’cie w formacie JSON - Kotlin + Spring Boot [Link do commita](https://github.com/mario343/proj-obiektowe/commit/cbad346936cbc1a5d4ad4bb3d6c038f4b66f5dc9)

:white_check_mark: 3.5 Należy stworzyć klasę do autoryzacji (mock) jako Singleton w
formie eager [Link do commita](https://github.com/mario343/proj-obiektowe/commit/cbad346936cbc1a5d4ad4bb3d6c038f4b66f5dc9)

:white_check_mark: 4.0 Należy obsłużyć dane autoryzacji przekazywane przez użytkownika [Link do commita](https://github.com/mario343/proj-obiektowe/commit/cbad346936cbc1a5d4ad4bb3d6c038f4b66f5dc9)

:x: 4.5 Należy wstrzyknąć singleton do głównej klasy via @Autowired

:x: 5.0 Obok wersji Eager do wyboru powinna być wersja Singletona w wersji
lazy

Kod: 03-springboot

[DEMO](https://github.com/mario343/proj-obiektowe/blob/main/demos/zadanie3.gif)

**Zadanie 4** Echo - Go

Należy stworzyć aplikację w Go na frameworku echo. Aplikacja ma mieć
jeden endpoint, minimum jedną funkcję proxy, która pobiera dane np. o
pogodzie, giełdzie, etc. (do wyboru) z zewnętrznego API. Zapytania do
endpointu można wysyłać w jako GET lub POST.

:white_check_mark: 3.0 Należy stworzyć aplikację we frameworki echo w j. Go, która będzie
miała kontroler Pogody, która pozwala na pobieranie danych o pogodzie
(lub akcjach giełdowych) [Link do commita](https://github.com/mario343/proj-obiektowe/commit/c05f4b57dfab0d517e855cc056d515ed402f8c32)

:white_check_mark: 3.5 Należy stworzyć model Pogoda (lub Giełda) wykorzystując gorm, a
dane załadować z listy przy uruchomieniu [Link do commita](https://github.com/mario343/proj-obiektowe/commit/c05f4b57dfab0d517e855cc056d515ed402f8c32)

:x: 4.0 Należy stworzyć klasę proxy, która pobierze dane z serwisu
zewnętrznego podczas zapytania do naszego kontrolera

:x: 4.5 Należy zapisać pobrane dane z zewnątrz do bazy danych

:x: 5.0 Należy rozszerzyć endpoint na więcej niż jedną lokalizację
(Pogoda), lub akcje (Giełda) zwracając JSONa

Kod: 04-go

[DEMO](https://github.com/mario343/proj-obiektowe/blob/main/demos/zadanie4.gif)

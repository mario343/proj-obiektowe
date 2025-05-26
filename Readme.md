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

**Zadanie 5** React

Wszystkie wymagania do oceny 4.0 zostały spełnione. Proszę zobaczyć repozytorium z ebiznesu:
[To zadanie zostało wykonane tutaj](https://github.com/mario343/ebiznes/tree/main/05-react-06-tests)
[Pełny opis zadania można znaleźć tutaj](https://github.com/mario343/ebiznes/blob/main/README.md)

**Zadanie 6** Sonar

Wszystkie wymagania do oceny 5.0 zostały spełnione. Proszę zobaczyć repozytorium z ebiznesu:

[To zadanie zostało wykonane tutaj](https://github.com/mario343/ebiznes/tree/main/05-react-06-tests) oraz [tutaj](https://github.com/mario343/ebiznes/tree/main/07-sonar)
[Pełny opis zadania można znaleźć tutaj](https://github.com/mario343/ebiznes/blob/main/README.md)

:white_check_mark: 3.0 Należy dodać eslint w hookach gita. [Link do commita](https://github.com/mario343/ebiznes/commit/3cc44a3bdace0e4cdf0594c0506c08f1fe12fd51)

:white_check_mark: 3.5 Należy wyeliminować wszystkie bugi w kodzie w Sonarze (kod
aplikacji klienckiej) [Link do commita](https://github.com/mario343/ebiznes/commit/d2f2ee71a57857f69262341fd0449b3fc4184204)

:white_check_mark: 4.0 Należy wyeliminować wszystkie zapaszki w kodzie w Sonarze (kod
aplikacji klienckiej) [Link do commita](https://github.com/mario343/ebiznes/commit/d2f2ee71a57857f69262341fd0449b3fc4184204)

:white_check_mark: 4.5 Należy wyeliminować wszystkie podatności oraz błędy bezpieczeństwa
w kodzie w Sonarze (kod aplikacji klienckiej) [Link do commita](https://github.com/mario343/ebiznes/commit/d2f2ee71a57857f69262341fd0449b3fc4184204)

:white_check_mark: 5.0 Zredukować duplikaty kodu do 0% [Link do commita](https://github.com/mario343/ebiznes/commit/d2f2ee71a57857f69262341fd0449b3fc4184204)

FRONTEND

[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=mario343_frontend)](https://sonarcloud.io/summary/new_code?id=mario343_frontend)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=mario343_frontend&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=mario343_frontend)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=mario343_frontend&metric=bugs)](https://sonarcloud.io/summary/new_code?id=mario343_frontend)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=mario343_frontend&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=mario343_frontend)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=mario343_frontend&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=mario343_frontend)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=mario343_frontend&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=mario343_frontend)

BACKEND

[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=mario343_backend)](https://sonarcloud.io/summary/new_code?id=mario343_backend)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=mario343_backend&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=mario343_backend)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=mario343_backend&metric=bugs)](https://sonarcloud.io/summary/new_code?id=mario343_backend)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=mario343_backend&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=mario343_backend)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=mario343_backend&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=mario343_backend)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=mario343_backend&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=mario343_backend)

[DEMO](https://github.com/mario343/ebiznes/blob/main/demos/zadanie7.gif)

**Zadanie 7** Vapor (swift)

Proszę napisać prostą aplikację w Vaporze, wykorzystując Leaf jako
silnik szablonów or Fluent jako ORM. Proszę stworzyć trzy modele oraz
CRUD dla każdego z nich. Należy stworzyć model z minimum jedną
relacją. CRUD powinien mieć odzwierciedlenie w szablonach.

:white_check_mark: 3.0 Należy stworzyć kontroler wraz z modele Produktów zgodny z CRUD w
ORM Fluent. [Link do commita](https://github.com/mario343/proj-obiektowe/commit/1f77b9ed1f4da7a85b909df0dd2233d6d01ad4c4)

:white_check_mark: 3.5 Należy stworzyć szablony w Leaf. [Link do commita](https://github.com/mario343/proj-obiektowe/commit/1f77b9ed1f4da7a85b909df0dd2233d6d01ad4c4)

:x: 4.0 Należy stworzyć drugi model oraz kontroler Kategorii wraz z
relacją. [Link do commita]()

:x: 4.5 Należy wykorzystać Redis do przechowywania danych. [Link do commita]()

:x: 5.0 Wrzucić aplikację na heroku. [Link do commita]()

Kod: 07-vapor

[DEMO](https://github.com/mario343/proj-obiektowe/blob/main/demos/zadanie7.gif)

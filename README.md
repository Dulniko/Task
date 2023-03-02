# Task API
> Aplikacja back-end w technologii Python, Django, Django rest framework i Postgresql. Projekt zawiera API służące do zarządzania zadaniami (tasks) oraz historią zmian tych zadań (history). Zadania są identyfikowane przez unikalne identyfikatory ID i posiadają nazwę (name), opis (description), status (status) oraz przydzielonego użytkownika (assigned_user). Historia zmian zawiera informacje o zmianach dotyczących danego zadania (task), takie jak nazwa (name), opis (description), status (status), przydzielony użytkownik (assigned_user) oraz datę od kiedy zadanie było ważne (valid_from) w tych parametrach i do kiedy (valid_until). Aplikacja pozwala na dodawanie, edycję, usuwanie, filtrowanie i wyświetlanie szczegółów zadań. Dodatkowo, aplikacja umożliwia wyświetlanie historii zmian zadań.

## Spis
* [Wymagania](#wymagania)
* [Instalacja](#Instalacja)
* [Użytkowanie](#Użytkowanie)
* [Rejestracja i logowanie](#Rejestracja)
* [Testy](#Testy)

## Wymagania
Do uruchomienia aplikacji potrzebny jest zainstalowany Python 3.8 lub nowszy oraz baza danych PostgreSQL.

## Instalacja
1. Sklonuj repozytorium aplikacji.
2. Utwórz wirtualne środowisko Pythona, np:
python -m venv venv
3. Aktywuj wirtualne środowisko, np:
source venv/bin/activate
4. Zainstaluj wymagane zależności:
pip install -r requirements.txt
5. Skonfiguruj bazę danych w pliku settings.py. Wprowadź odpowiednie dane do sekcji DATABASES bądź utwórz plik .env i tam zdefiniuj zmienne, zmień równieź klucz.
6. Wykonaj migracje bazy danych:
python manage.py migrate
7. Uruchom serwer:
python manage.py runserver
Aplikacja będzie dostępna pod adresem http://127.0.0.1:8000/

## Uruchomienie z użyciem dockera
1. Upewnij się czy masz zainstalowanego dockera/docker-compose, jeśli nie przejdź na adres https://docs.docker.com/desktop/ i postępuj zgodnie z instrukcjami instalacji opisanymi na stronie w zależności od twojego systemu operacyjnego.
2. Skonfiguruj plik docker-compose.yml dodając plik .env w którym zdefiniujesz zmienne bądź zdefiniuj je bezpośrednio w pliku aby uzyskać dostęp do bazy danych.  
3. Wykonaj migrację bazy: 
docker-compose run web python manage.py migrate
4. Uruchom kontenery a tym samym serwer:
docker-compose up

## Użytkowanie
API składa się z dwóch końcówek 
- /tasks 
- /history

## Przykładowe odpytania końcowe /tasks
## 1. Pobierz listę zadań
### a) GET /tasks/

Przykładowa odpowiedź:
```
[
    {
        "id": 1,
        "name": "test",
        "description": "test1",
        "status": "New",
        "assigned_user": null,
        "created_at": "2023-03-01 15:10:42"
    },
    {
        "id": 2,
        "name": "test2",
        "description": "test2.4",
        "status": "New",
        "assigned_user": 1,
        "created_at": "2023-03-01 15:11:42"
    }
]
```
### b) curl http://localhost:8000/tasks/

Przykładowa odpowiedź:
```
[{"id":1,"name":"test","description":"test1","status":"New","assigned_user":null,"created_at":"2023-03-01 15:10:42"},{"id":3,"name":"test3","description":"test3.2","status":"New","assigned_user":1,"created_at":"2023-03-01 15:14:22"}]
```
## 2. Pobierz szczegóły zadania
### a)GET /tasks/{id}/

Przykładowa odpowiedź:
```
{
    "id": 1,
    "name": "test",
    "description": "test1",
    "status": "New",
    "assigned_user": null,
    "created_at": "2023-03-01 15:10:42"
}
```
### b)curl http://localhost:8000/tasks/1/
Przykładowa odpowiedź:
```
{"id":1,"name":"test","description":"test1","status":"New","assigned_user":null,"created_at":"2023-03-01 15:10:42"}
```
## 3. Dodaj zadanie
### POST /tasks/
```
{
    "name": "Przykładowe zadanie",
    "description": "Opis przykładowego zadania",
    "status": "New",
    "assigned_user": 1
}
```
Przykładowa odpowiedź:
```
{
    "id": 3,
    "name": "Przykładowe zadanie",
    "description": "Opis przykładowego zadania",
    "status": "New",
    "assigned_user": 1,
    "created_at": "2023-03-01 15:13:05"
}
```
## 4. Zaktualizuj zadanie
### PUT /tasks/{id}/
```
{
    "name": "Nowa nazwa zadania",
    "description": "Nowy opis zadania",
    "status": "W toku",
    "assigned_user": 2
}
```
Przykładowa odpowiedź:
```
{
    "id": 1,
    "name": "Nowa nazwa zadania",
    "description": "Nowy opis zadania",
    "status": "W toku",
    "assigned_user": 2,
    "created_at": "2022-02-28 15:20:00"
}
```
## 5. Usuwa zadanie o podanym id
### DELETE /tasks/{id}/

## Parametry do filtrowania:
- id - id zadania (np. /tasks/?id=1)
- name - nazwa zadania (np. /tasks/?name=Zadanie1)
- description - opis zadania (np. /tasks/?description=Opis1)
- status - status zadania (np. /tasks/?status=New)
- assigned_user - id użytkownika przypisanego do zadania (np. /tasks/?assigned_user=1)

## Sortowanie:
- ordering - pozwala na sortowanie po wybranym polu (np. /tasks/?ordering=name)

## Wyszukiwanie:
- search - pozwala na wyszukiwanie w polach name i description (np. /tasks/?search=Zadanie1)


## Przykładowe odpytania końcowe /history

## 1. Pobiera wszystkie wpisy w historii zmian w zadaniach
### GET /history/ 

Przykładowa odpowiedź:
```
[
    {
        "id": 1,
        "task": 2,
        "name": "test2",
        "description": "test2",
        "status": "New",
        "assigned_user": 1,
        "valid_from": "2023-03-01 15:11:11",
        "valid_until": "2023-03-01 15:11:37"
    },
    {
        "id": 2,
        "task": 2,
        "name": "test2",
        "description": "test2.2",
        "status": "New",
        "assigned_user": 1,
        "valid_from": "2023-03-01 15:11:37",
        "valid_until": "2023-03-01 15:11:40"
    },
    {
        "id": 3,
        "task": 2,
        "name": "test2",
        "description": "test2.3",
        "status": "New",
        "assigned_user": 1,
        "valid_from": "2023-03-01 15:11:40",
        "valid_until": "2023-03-01 15:11:42"
    }
]
```
## 2. Pobiera wpis w historii zmian w zadaniu o podanym id
### GET /history/{id}/ 

Przykładowa odpowiedź:
```
{
    "id": 4,
    "task": 3,
    "name": "test3",
    "description": "test3",
    "status": "New",
    "assigned_user": 1,
    "valid_from": "2023-03-01 15:13:05",
    "valid_until": "2023-03-01 15:14:22"
}
```
## Parametry do filtrowania:
- task - id zadania, którego dotyczy wpis w historii zmian (np. /history/?task=1)
- valid_from - pobiera wpisy w historii zmian z datą od określonej wartości (np. /history/?valid_from=2022-01-01)
- valid_until - pobiera wpisy w historii zmian do daty określonej wartości (np. /history/?valid_until=2022-01-01)

## Rejestracja
Aplikacja umożliwia rejestrację i logowanie użytkowników pod końcówkami url
- /register
- /login
- /logout

## Testy
Skonfiguruj bezpośrednio plik test_settings.py, bądź zdefiniuj zmienne w .env, aby testy miały dostęp do bazy. (zostaw jedynie localhost).
Następnie aby uruchomić testy, użyj komendy
```
pytest
```
w katalogu aplikacji
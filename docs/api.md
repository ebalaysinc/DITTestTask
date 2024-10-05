# Описание API
## Авторизация
Для всех методов требуется авторизация. Токен указывается в Authorization заголовке (в формате: 'Authorization: Token 123456...abcdef')
### POST /api/login/
Принимает username и password. Если логин/пароль неверный, то вернёт status: False и error. Иначе вернёт токен и status: True
- Стандартный запрос:
```
{
    "username": "foo", 
    "password": "bar"
}
```
- Стандартный ответ:
```
{
    "status": true,
    "token": "some-token"
}
```
- Ответ с ошибкой:
```
{
    "status": false,
    "error": "some-error"
}
```
- Список ошибок
```
CredentialsMissedError - отсутствуют логин и/или пароль в запросе
BadCredentialsError - неверный логин и/или пароль
```
### Регистрация новых пользователей, удаление, смена пароля и т.д.
Происходит через админ панель Django. Подробнее [здесь](./deploy.md#авторизация-регистрация-и-тд)
## Получение данных
### GET /api/getAllTitles/
Ничего не принимает, возвращает все записанные модели Title
- Стандартный ответ:
```
{
    "status": true,
    "titles": [
        {
            "id": 12345678,
            "name": "Default Title Name",
            "link": "https://example.com/"
        }, ...
    ]
}
```
### GET /api/getAllChapters/
Принимает ID тайтла, возвращает все модели Chapter
- Стандартный запрос:
```
{
    "id": 12345678
}
```
- Стандартный ответ:
```
{
    "status": true,
    "chapters": [
        {
            "id": 12345678,
            "name": "Default Chapter Name",
            "status": False,
            "original": "https://example.com/"
        }, ...
    ]
}
```
- Ответ с ошибкой:
```
{
    "status": false,
    "error": "some-error"
}
```
- Список ошибок
```
NoDataProvidedError - в запросе отсутствуют необходимые данные и/или они указаны неверно
TitleNotExistError - тайтла с указанным id не существует
```
### GET /api/getChapter/
Принимает ID главы, возвращает одну главу с указанным ID, если она существует
- Стандартный запрос:
```
{
    "id": 12345678
}
```
- Стандартный ответ:
```
{
    "status": true,
    "chapter": {
            "id": 12345678,
            "name": "Default Chapter Name",
            "status": False,
            "original": "https://example.com/"
    }
}
```
- Ответ с ошибкой:
```
{
    "status": false,
    "error": "some-error"
}
```
- Список ошибок
```
NoDataProvidedError - в запросе отсутствуют необходимые данные и/или они указаны неверно
ChapterNotExistError - главы с указанным id не существует
```
### GET /api/getAllWorkers/
Принимает ID главы, возвращает все модели Worker
- Стандартный запрос:
```
{
    "id": 12345678
}
```
- Стандартный ответ:
```
{
    "status": true,
    "workers": [
        {
            "id": 12345678,
            "nickname": "John Doe",
            "contact": "TG: @durov",
            "occupation": "Переводчик"
        }, ...
    ]
}
```
- Ответ с ошибкой:
```
{
    "status": false,
    "error": "some-error"
}
```
- Список ошибок
```
NoDataProvidedError - в запросе отсутствуют необходимые данные и/или они указаны неверно
TitleNotExistError - тайтла с указанным id не существует
```
## Работа с тайтлами
### POST /api/title/createTitle/
Принимает данные тайтла и возвращает экземпляр тайтла в случае успеха. В ином случае - ошибку
- Стандартный запрос:
```
{
    "name": "Lorem ipsum",
    "link": "https://example.com/"
}
```
- Стандартный ответ:
```
{
    "status": true,
    "title": {
        "id": 12345678,
        "name": "Default Title Name",
        "link": "https://example.com/"
    }
}
```
- Ответ с ошибкой:
```
{
    "status": false, 
    "error": "some-error"
}
```
- Список ошибок
```
NoDataProvidedError - в запросе отсутствуют необходимые данные
```
### POST /api/title/deleteTitle/
Принимает ID тайтла и возвращает status: true в случае успеха. В ином случае - ошибку
- Стандартный запрос:
```
{
    "id": 12345678
}
```
- Стандартный ответ:
```
{
    "status": true
}
```
- Ответ с ошибкой:
```
{
    "status": false, 
    "error": "some-error"
}
```
- Список ошибок
```
NoDataProvidedError - в запросе отсутствуют необходимые данные и/или они указаны неверно
TitleNotExistError - тайтла с указанным id не существует
```
### POST /api/title/editTitle/
Принимает ID тайтла и данные для изменения и возвращает обновлённый экземпляр тайтла в случае успеха. В ином случае - ошибку
- Стандартный запрос:
```
{
    "id"*: 12345678,
    "name": "Ipsum lorem",
    "link": "https://example.com/"
}
```
*Данные, помеченные звёздочкой - обязательны*
- Стандартный ответ:
```
{
    "status": true,
    "title": {
        "id": 12345678,
        "name": "Default Title Name",
        "link": "https://example.com/"
    }
}
```
- Ответ с ошибкой:
```
{
    "status": false,
    "error": "some-error"
}
```
- Список ошибок
```
NoDataProvidedError - в запросе отсутствуют необходимые данные и/или они указаны неверно
TitleNotExistError - тайтла с указанным id не существует
```
## Работа с главами
### POST /api/chapter/createChapter/
Принимает на вход данные главы и ID тайтла, возвращает экземпляр главы
- Стандартный запрос:
```
{
    "name": "Lorem ipsum",
    "link": "https://example.com/",
    "status": False,
    "original": "https://example.com/"
}
```
- Стандартный ответ:
```
{
    "status": true,
    "chapter": {
        "id": 12345678,
        "name": "Lorem ipsum",
        "status": False,
        "original": "https://example.com/"
    }
}
```
- Ответ с ошибкой:
```
{
    "status": false, 
    "error": "some-error"
}
```
- Список ошибок
```
NoDataProvidedError - в запросе отсутствуют необходимые данные
TitleNotExistError - тайтла с указанным id не существует
```
### POST /api/chapter/deleteChapter/
Принимает ID главы и возвращает status: true в случае успеха. В ином случае - ошибку
- Стандартный запрос:
```
{
    "id": 12345678
}
```
- Стандартный ответ:
```
{
    "status": true
}
```
- Ответ с ошибкой:
```
{
    "status": false, 
    "error": "some-error"
}
```
- Список ошибок
```
NoDataProvidedError - в запросе отсутствуют необходимые данные и/или они указаны неверно
ChapterNotExistError - главы с указанным id не существует
```
### POST /api/chapter/editChapterName/
Принимает ID главы и данные для изменения и возвращает обновлённый экземпляр главы в случае успеха. В ином случае - ошибку
- Стандартный запрос:
```
{
    "id"*: 12345678,
    "name": "Ipsum lorem",
    "status": 0/1 (0 приравнивается к false, 1 к true),
    "original": "https://example.com"
}
```
*Данные, помеченные звёздочкой - обязательны*
- Стандартный ответ:
```
{
    "status": true,
    "chapter": {
        "id": 12345678,
        "status": false,
        "original": "https://example.com"
    }
}
```
- Ответ с ошибкой:
```
{
    "status": false,
    "error": "some-error"
}
```
- Список ошибок
```
NoDataProvidedError - в запросе отсутствуют необходимые данные и/или они указаны неверно
ChapterNotExistError - главы с указанным id не существует
```
## Работа с работниками
### POST /api/worker/createWorker/
Принимает на вход данные работника и ID главы, возвращает экземпляр работника
- Стандартный запрос:
```
{
    "id": 12345678,
    "nickname": "John Doe",
    "contact": "TG: @durov",
    "occupation": "Переводчик"
}
```
- Стандартный ответ:
```
{
    "status": true,
    "worker": {
        "id": 12345678,
        "nickname": "John Doe",
        "contact": "TG: @durov",
        "occupation": "Переводчик"
    }
}
```
- Ответ с ошибкой:
```
{
    "status": false, 
    "error": "some-error"
}
```
- Список ошибок
```
NoDataProvidedError - в запросе отсутствуют необходимые данные
ChapterNotExistError - главы с указанным id не существует
```
### POST /api/worker/deleteWorker/
Принимает ID работника и возвращает status: true в случае успеха. В ином случае - ошибку
- Стандартный запрос:
```
{
    "id": 12345678
}
```
- Стандартный ответ:
```
{
    "status": true
}
```
- Ответ с ошибкой:
```
{
    "status": false, 
    "error": "some-error"
}
```
- Список ошибок
```
NoDataProvidedError - в запросе отсутствуют необходимые данные и/или они указаны неверно
WorkerNotExistError - главы с указанным id не существует
```
### POST /api/worker/editWorkerInfo/
Принимает ID работника и данные для изменения и возвращает обновлённый экземпляр работника в случае успеха. В ином случае - ошибку
- Стандартный запрос:
```
{
    "id"*: 12345678,
    "nickname": "John Doe",
    "contact": "TG: @durov",
    "occupation": "Переводчик"
}
```
*Данные, помеченные звёздочкой - обязательны*
- Стандартный ответ:
```
{
    "status": true,
    "worker": {
        "id": 12345678,
        "nickname": "John Doe",
        "contact": "TG: @durov",
        "occupation": "Переводчик"
    }
}
```
- Ответ с ошибкой:
```
{
    "status": false,
    "error": "some-error"
}
```
- Список ошибок
```
NoDataProvidedError - в запросе отсутствуют необходимые данные и/или они указаны неверно
WorkerNotExistError - работника с указанным id не существует
```
## Частые ошибки
- **Запрос возвращает `{"detail":"Authentication credentials were not provided."}`.** В заголовке Authorization не указан токен или указан неверно.
- **Запрос возвращает `{"detail":"Method *** not allowed."}`.** Выбран неправильный метод. Сверьтесь с документацией API.
## Развёртывание через Docker
### Разработка
1. Переименуйте .env.dev-sample в .env.dev
2. Измените переменные среды в .env.dev и docker-compose.yml
3. Поднимите контейнеры:
`docker-compose up -d --build`
4. Проверьте доступность сайта на http://127.0.0.1:8000
### Продакшен
1. Переименуйте .env.prod в .env.prod и .env.prod.db-sample в .env.prod.db
2. Измените переменные среды в .env.prod и .env.prod.db
3. Поднимите контейнеры:
`docker-compose -f docker-compose.prod.yml up -d --build`
4. Сделайте миграцию и collectstatic
```
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```
5. Проверьте доступность сайта на http://127.0.0.1
## Авторизация, регистрация и т.д.
1. Создайте суперпользователя: `docker-compose (-f docker-compose.prod.yml) exec web python manage.py createsuperuser`
2. Войдите под введёнными данными на http://127.0.0.1(:8000)/admin/
3. Добавьте нового пользователя в Users
4. Проверьте возможность авторизации под новым пользователем
## Домашняя работа 27.2.
- Описан Dockerfile для запуска контейнера с проектом.
- Создан Docker Compose Django-проект с БД PostgreSQL.
- Добавлен в docker-compose.yaml работу с Redis.
- Добавлен в docker-compose.yaml работу с Celery.
- Работа проверена с помощью Postman и в браузере.

### Основные приложения
- Ubuntu 24.04 LTS
- Python 3.12.3
- Poetry 1.8.2
- git 2.43.0
- VSCode 1.96.0 (Windows 11)
- PostgreSQL 16.3
- Docker 4.37.0

### Инструкция для развертывания проекта

#### Клонирование проекта:
```
git clone https://github.com/AidarPutilov/kurs7.git
```

#### Переход в каталог
```
cd kurs7
```

#### Базовые настройки
```
Ввести настройки django, сервера PostgreSQL, сервера Redis в файле ".env.sample". Переименовать файл в ".env".
```

#### Создание и запуск контейнера
```
docker-compose up -d --build
```

#### Остановка и удаление контейнера
```
docker-compose down
```

#### Доступ к документации
```
http://127.0.0.1:8000/swagger/ - Swagger
http://127.0.0.1:8000/redoc/ - Redoc
```

### Запросы User
```
http://127.0.0.1:8000/users/register/ - Регистрация пользователя
http://127.0.0.1:8000/users/login/ - Авторизация, получение токена
http://127.0.0.1:8000/users/list/ - Список пользователей
http://127.0.0.1:8000/users/view/<pk>/ - Просмотр пользователя
http://127.0.0.1:8000/users/update/<pk>/ - Редактирование пользователя
http://127.0.0.1:8000/users/delete/<pk>/ - Удаление пользователя
```

### Запросы Habit
```
http://127.0.0.1:8000/main/ - LIST, CREATE
http://127.0.0.1:8000/main/<pk>/ - RETRIEVE, PUT, PATCH, DELETE
http://127.0.0.1:8000/main/public/ - Список публичных записей
```

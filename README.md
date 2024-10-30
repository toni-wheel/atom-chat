# Atom Chat

## Описание

Atom Chat — это сервис для создания и управления приватными чатами. Он разработан с использованием технологий Vue.js (фронтенд) и FastAPI (бэкенд), а данные хранятся в PostgreSQL. С помощью Atom Chat пользователи могут обмениваться сообщениями, создавать каналы и управлять участниками чатов.

## Визуал

### Регистрация нового пользователя

![Screenshot 2](https://s3.timeweb.cloud/6dfc936a-codelab.pro/atom-chat/Screenshot_2.png)

### Регистрация существующего пользователя

![Screenshot 1](https://s3.timeweb.cloud/6dfc936a-codelab.pro/atom-chat/Screenshot_1.png)

### Вход в чат в качестве модератора. Доступны все каналы, списки пользователей и кнопка "Заблокировать".

![Screenshot 3](https://s3.timeweb.cloud/6dfc936a-codelab.pro/atom-chat/Screenshot_3.png)

### Блокировка неугодных пользователей

![Screenshot 4](https://s3.timeweb.cloud/6dfc936a-codelab.pro/atom-chat/Screenshot_4.png)

### Заблокированный пользователь не может залогиниться (также есть рут на запрет отправки сообщения)

![Screenshot 5](https://s3.timeweb.cloud/6dfc936a-codelab.pro/atom-chat/Screenshot_5.png)

### Пользователь видит только те чаты, в которые добавлен

![Screenshot 7](https://s3.timeweb.cloud/6dfc936a-codelab.pro/atom-chat/Screenshot_7.png)

## Структура Базы Данных

### Пользователи (Users)

- **id:** Уникальный идентификатор пользователя.
- **username:** Уникальное имя пользователя.
- **password:** Хешированный пароль пользователя.
- **is_moderator:** Флаг, указывающий, является ли пользователь модератором.
- **is_active:** Флаг, указывающий, активен ли пользователь.

### Сообщения (Messages)

- **id:** Уникальный идентификатор сообщения.
- **content:** Содержимое сообщения.
- **channel_id:** Идентификатор канала, в котором отправлено сообщение.
- **user_id:** Идентификатор пользователя, отправившего сообщение.
- **created_at:** Дата и время отправки сообщения.

### Каналы (Channels)

- **id:** Уникальный идентификатор канала.
- **name:** Название канала (должно быть уникальным).
- **is_private:** Флаг, указывающий, является ли канал приватным.
- **created_at:** Дата и время создания канала.

### Принадлежность (Memberships)

- **id:** Уникальный идентификатор записи о принадлежности.
- **user_id:** Идентификатор пользователя, присоединившегося к каналу.
- **channel_id:** Идентификатор канала, к которому присоединился пользователь.
- **joined_at:** Дата и время присоединения пользователя к каналу.

## API Эндпоинты

### Пользователи (Users)

- **Регистрация пользователя:** POST /user/register
- **Авторизация пользователя:** POST /user/login
- **Получить пользователей:** GET /user/
- **Удалить пользователей:** DELETE /user/
- **Получить пользователя по ID:** GET /user/{user_id}
- **Обновить пользователя по ID:** PATCH /user/{user_id}
- **Удалить пользователя по ID:** DELETE /user/{user_id}
- **Заблокировать пользователя:** POST /user/block/{user_id}

### Сообщения (Messages)

- **Создать сообщение:** POST /messages/
- **Получить сообщения:** GET /messages/
- **Удалить сообщения:** DELETE /messages/
- **Получить сообщение по ID:** GET /messages/{message_id}
- **Обновить сообщение по ID:** PATCH /messages/{message_id}
- **Удалить сообщение по ID:** DELETE /messages/{message_id}
- **Получить сообщения по каналу:** GET /messages/channel/{channel_id}

### Каналы (Channels)

- **Создать канал:** POST /channels/
- **Получить каналы:** GET /channels/
- **Удалить каналы:** DELETE /channels/
- **Получить канал по ID:** GET /channels/{channel_id}
- **Обновить канал по ID:** PATCH /channels/{channel_id}
- **Удалить канал по ID:** DELETE /channels/{channel_id}

### Принадлежность (Memberships)

- **Создать принадлежность:** POST /memberships/
- **Получить принадлежности:** GET /memberships/
- **Удалить принадлежности:** DELETE /memberships/
- **Обновить принадлежность по ID:** PATCH /memberships/{membership_id}
- **Удалить принадлежность по ID:** DELETE /memberships/{membership_id}
- **Получить пользователей по каналу:** GET /memberships/channel/{channel_id}/users
- **Получить каналы по пользователю:** GET /memberships/user/{user_id}/channels

## Деплой проекта

### Подготовка бэкенда

cd api
python -m venv venv
source venv/Scripts/activate
pip install -r deps.txt
alembic init migrations
alembic revision --autogenerate -m "Старт"
alembic upgrade head
uvicorn main:app --reload

Доступен по порту http://localhost:8000/
Эндпоинты http://localhost:8000/docs

### Подготовка фронтенда

cd clinet
npm install
npm run build

Доступен в файле index.html (его необходимо поместить на корневую папку веб-сервера)

### Запуск на сервере

Загрузить папку с проектом на сервер

cd api

docker-compose up -d

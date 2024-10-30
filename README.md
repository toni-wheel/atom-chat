# Atom Chat

## Описание

Atom Chat — это сервис для создания и управления приватными чатами. Он разработан с использованием технологий Vue.js и FastAPI, а данные хранятся в PostgreSQL. С помощью Atom Chat пользователи могут обмениваться сообщениями, создавать каналы и управлять участниками чатов.

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

## Визуал

![Screenshot 1](https://s3.timeweb.cloud/6dfc936a-codelab.pro/atom-chat/Screenshot_1.png)
![Screenshot 2](https://s3.timeweb.cloud/6dfc936a-codelab.pro/atom-chat/Screenshot_2.png)
![Screenshot 3](https://s3.timeweb.cloud/6dfc936a-codelab.pro/atom-chat/Screenshot_3.png)
![Screenshot 4](https://s3.timeweb.cloud/6dfc936a-codelab.pro/atom-chat/Screenshot_4.png)
![Screenshot 5](https://s3.timeweb.cloud/6dfc936a-codelab.pro/atom-chat/Screenshot_5.png)
![Screenshot 6](https://s3.timeweb.cloud/6dfc936a-codelab.pro/atom-chat/Screenshot_6.png)
![Screenshot 7](https://s3.timeweb.cloud/6dfc936a-codelab.pro/atom-chat/Screenshot_7.png)

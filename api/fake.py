# Фейковая база данных

fake_tasks = [
    {"id": 1, "title": "Подготовить отчет", "description": "Составить еженедельный отчет по продажам", "completed": False},
    {"id": 2, "title": "Обновить сайт", "description": "Обновить главную страницу сайта с новыми продуктами", "completed": True},
    {"id": 3, "title": "Ответить на письма", "description": "Ответить на все непрочитанные электронные письма", "completed": False},
    {"id": 4, "title": "Провести собрание", "description": "Организовать ежемесячное собрание команды", "completed": False},
    {"id": 5, "title": "Закупить канцелярские товары", "description": "Закупить необходимые канцелярские товары для офиса", "completed": True},
]

# Функция поиска по ID
def find_tasks(id: str, arr: list):
    found_tasks = []
    for task in arr:
        if task.get("id") == id:
            found_tasks.append(task)
    return found_tasks
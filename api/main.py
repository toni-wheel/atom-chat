# Точка входа

from fastapi import FastAPI
from routers.user import user_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title = "Atom Chat"
)

# Настройка CORS
origins = [
    "http://localhost:5173",  # Фронтенд URL
    "http://localhost:8000",  # Бэкенд URL
    # Другие допустимые источники
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)


@app.get("/")
def get_home():
    return {"data": "Привет, мир"}

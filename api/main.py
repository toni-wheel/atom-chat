# Точка входа

from fastapi import FastAPI
from routers import router

app = FastAPI(
    title = "Todolist App"
)

app.include_router(router)

@app.get("/")
def get_home():
    return {"data": "Привет, мир"}

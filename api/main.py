# Точка входа

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from routers.user import user_router
from routers.message import message_router
from routers.channel import channel_router
from fastapi.middleware.cors import CORSMiddleware
from chat import manager


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
app.include_router(message_router)
app.include_router(channel_router)


@app.get("/")
def get_home():
    return {"data": "Привет, мир"}


@app.websocket("/ws/{channel_id}")
async def websocket_endpoint(websocket: WebSocket, channel_id: int):
    await manager.connect(websocket, channel_id)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_message(data, channel_id)
    except WebSocketDisconnect:
        manager.disconnect(websocket, channel_id)

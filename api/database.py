# Настройки подключения к базе данных

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import settings

Base = declarative_base()

# Создание синхронного подключения к базе данных
engine = create_engine(
    # URL для подключения к базе данных, берется из настроек
    url=settings.DATABASE_URL_psycopg,
    # Логирование SQL-запросов в консоль для отладки
    echo=False,
    # Максимальное количество соединений в пуле
    pool_size=5,
    # Максимальное количество дополнительных соединений, которые могут быть созданы сверх пула
    max_overflow=10
)

Session = sessionmaker(bind=engine)
db = Session()


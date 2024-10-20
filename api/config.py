# Настройки базы данных

from pydantic_settings import BaseSettings, SettingsConfigDict

# Создаем класс настроек, наследуемый от BaseSettings из Pydantic
class Settings(BaseSettings):
    # Определяем переменные для подключения к базе данных
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    # Определяем свойство для генерации URL подключения к базе данных с использованием psycopg
    @property
    def DATABASE_URL_psycopg(self):
        # Формируем строку подключения в формате, подходящем для psycopg2
        return f"postgresql+psycopg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    
    # Указываем файл окружения, откуда будут загружаться переменные
    model_config = SettingsConfigDict(env_file=".env")

# Создаем экземпляр класса Settings, автоматически загружающий переменные из .env файла
settings = Settings()

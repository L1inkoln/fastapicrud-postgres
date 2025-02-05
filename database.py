from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Настройки подключения
DATABASE_URL = (
    "postgresql+psycopg2://postgres:12345@localhost:5432/mydb?client_encoding=utf8"
)

# Создаем движок SQLAlchemy
engine = create_engine(DATABASE_URL)

# Создаем таблицы в базе данных
Base.metadata.create_all(engine)

# Настраиваем сессию для работы с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
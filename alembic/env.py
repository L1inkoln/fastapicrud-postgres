from logging.config import fileConfig
from sqlalchemy import create_engine
from alembic import context
from models import Base  # Импортируем Base из models.py

# Загружаем конфигурацию логов из alembic.ini
config = context.config
fileConfig(config.config_file_name)

# Подключаемся к базе данных
target_metadata = Base.metadata  # Используем метаданные из Base
sqlalchemy_url = config.get_main_option("sqlalchemy.url")

def run_migrations_offline():
    """Запуск миграций в оффлайн-режиме."""
    context.configure(
        url=sqlalchemy_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Запуск миграций в онлайн-режиме."""
    connectable = create_engine(sqlalchemy_url)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
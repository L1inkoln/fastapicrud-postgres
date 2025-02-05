from authx import AuthXConfig

# Конфигурация AuthX
authx_config = AuthXConfig(
    JWT_ALGORITHM="HS256",
    JWT_SECRET_KEY="your-secret-key",  # Замените на ваш секретный ключ
    JWT_TOKEN_LOCATION=["headers"],
)
from fastapi import FastAPI
from routers import users,login
import uvicorn
from authx import AuthX
from routers.login import init_cache
from config import authx_config  # Импортируем конфигурацию

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_cache() 

auth = AuthX(config=authx_config)

# Добавляем обработку ошибок AuthX в приложение
auth.handle_errors(app)
# Подключаем роутеры
app.include_router(users.router)
app.include_router(login.router)

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)




from pydantic import BaseModel

class UserLoginShema(BaseModel):
    username: str
    password: str

# Pydantic модель для создания пользователя
class UserCreate(BaseModel):
    name: str
    age: int
    username: str  # Добавляем username
    password: str  # Добавляем password

# Pydantic модель для ответа
class UserResponse(BaseModel):
    id: int
    name: str
    age: int
    username: str  # Добавляем username

    class Config:
        from_attributes = True  # Для совместимости с ORM
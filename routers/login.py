from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from schemas import UserLoginShema
from authx import AuthX, AuthXConfig, RequestToken
import bcrypt
from fastapi_cache.decorator import cache
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis


redis = aioredis.from_url("redis://localhost", encoding="utf-8", decode_responses=True)
async def init_cache():
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

router = APIRouter(tags=["auth"])

@cache()
async def get_cache():
    return 1

config = AuthXConfig(
    JWT_ALGORITHM="HS256",
    JWT_SECRET_KEY="SECRET_KEY",
    JWT_TOKEN_LOCATION=["headers"],
)

auth = AuthX(config=config)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

@router.post('/login')
@cache(expire=60)
async def login(creds: UserLoginShema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == creds.username).first()
    if user and verify_password(creds.password, user.password):
        token = auth.create_access_token(uid=str(user.id))
        return {"access_token": token}
    raise HTTPException(status_code=401, detail={"message": "Invalid credentials"})


@router.get("/protected", dependencies=[Depends(auth.get_token_from_request)])
@cache(expire=60)
async def get_protected(token: RequestToken = Depends()):
    try:
        auth.verify_token(token=token)
        return {"message": "Hello world!"}
    except Exception as e:
        raise HTTPException(status_code=401, detail={"message": str(e)}) from e
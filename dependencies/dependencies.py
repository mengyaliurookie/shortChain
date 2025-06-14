from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError,jwt
from typing import AsyncGenerator
from db.database import SessionLocal
from passlib.context import CryptContext
from contextlib import asynccontextmanager
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, status


pwd_context=CryptContext(schemes=['bcrypt'],deprecated='auto')

# 创建 OAuth2 密码承载器
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class PasslibHelper:

    @staticmethod
    def verity_password(plain_password:str, hashed_password:str):
        """对密码进行校验"""
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def hash_password(selfpassword:str)->str:
        return pwd_context.hash(selfpassword)

class AuthTokenHelper:
    """
    token编码与解码
    """
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    @staticmethod
    def token_encode(data:dict):
        return jwt.encode(data,AuthTokenHelper.SECRET_KEY,algorithm=AuthTokenHelper.ALGORITHM)
    @staticmethod
    def token_decode(token:str):
        payload=jwt.decode(token,AuthTokenHelper.SECRET_KEY,algorithms=[AuthTokenHelper.ALGORITHM])
        return payload

@asynccontextmanager
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    db_session=None
    try:
        db_session = SessionLocal()
        yield db_session
    finally:
        await db_session.close()

# 使用依赖项注入和yield，可以为每一个请求分配不同的会话对象。为了更好地管理项目中的所有依赖项，这里统一把所有依赖项都在dependencies包中进行了声明，


if __name__=="__main__":
    print(PasslibHelper.hash_password("123456"))

from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator
from db.database import SessionLocal


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    db_session=None
    try:
        db_session = SessionLocal()
        yield db_session
    finally:
        await db_session.close()

# 使用依赖项注入和yield，可以为每一个请求分配不同的会话对象。为了更好地管理项目中的所有依赖项，这里统一把所有依赖项都在dependencies包中进行了声明，

from sqlalchemy import select,update,delete
from sqlalchemy.ext.asyncio import AsyncSession
from models.model import User
from db.database import async_engine,Base



class UserServeries:

    @staticmethod
    async def get_user(async_session:AsyncSession,user_id:int):
        result=await async_session.execute(select(User).where(User.id==user_id))
        return result.scalars().first()

    @staticmethod
    async def get_user_by_name(async_session:AsyncSession,name:str):
        result=await async_session.execute((select(User).where(User.name==name)))


    @staticmethod
    async def get_users(async_session:AsyncSession):
        result=await async_session.execute(select(User).order_by(User.id))
        return result.scalars().fetchall()


    @staticmethod
    async def create_user(async_session:AsyncSession,**kwargs):
        new_user=User(**kwargs)
        async_session.add(new_user)
        await async_session.commit()
        return new_user

    @staticmethod
    async  def update_user(async_session:AsyncSession,user_id:int,**kwargs):
        response=update(User).where(User.id==user_id)
        result=await async_session.execute(response.values(**kwargs))
        await async_session.commit()
        return result


    async def delete_user(async_session:AsyncSession,user_id:int):
        response=await async_session.execute(delete(User).where(User.id==user_id))
        await async_session.commit()
        return response
    

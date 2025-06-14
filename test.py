from servies.user import UserServeries
from dependencies.dependencies import PasslibHelper
from sqlalchemy import func












if __name__ == '__main__':
    import asyncio
    from dependencies.dependencies import get_db_session
    async def create_admin_user():
        async with get_db_session() as db:
            await UserServeries.create_user(db,username='admin',password=PasslibHelper.hash_password("12345678"),created_at=func.now())
    asyncio.run(create_admin_user())
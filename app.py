from fastapi import FastAPI
from api.short import router_short
from api.user import router_user

app=FastAPI(title="FastAPI集成短链实战案例")

# 用于定义FastAPI的对象以及与初始化相关的路由注册操作
app.include_router(router_short)
app.include_router(router_user)
@app.on_event("startup")
async def startup_event():
    print("启动")
    from db.database import async_engine,Base
    from models.model import ShortUrl,  User
    async def init_create_table():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
    await init_create_table()


@app.on_event("shutdown")
async def shutdown_event():
    pass
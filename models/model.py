from db.database import Base
from sqlalchemy import Column,DateTime,func,Integer,String


class User(Base):
    # 指定本类映射到user表
    __tablename__='user'
    id=Column(Integer,primary_key=True,autoincrement=True)
    # 用户姓名
    username=Column(String(32),nullable=False)
    # 用户密码
    password=Column(String(64),nullable=False)
    # 创建时间
    created_at=Column(DateTime(),default=func.now())

class ShortUrl(Base):
    # 指定本类映射到short_url表
    __tablename__='short_url'
    id=Column(Integer,primary_key=True,autoincrement=True)
    # 短链标签
    short_tag=Column(String(32),nullable=False)
    # 短链地址
    short_url=Column(String(20))
    # 长链地址
    long_url=Column(String(255),nullable=False)
    # 访问次数
    visit_count=Column(Integer,nullable=True)
    # 创建时间
    created_at=Column(DateTime(),default=func.now())

    # 短链创建用户
    created_by=Column(String(32))
    # 短信内容
    msg_context=Column(String(255),nullable=False)
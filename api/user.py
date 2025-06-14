from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from dependencies.dependencies import get_db_session
from servies.user import UserServeries
from dependencies.dependencies import PasslibHelper,AuthTokenHelper
from datetime import datetime,timedelta
from schemes.schemes import SingShortUrlCreate
from utils.utils import generate_short_url
from servies.short import ShortServeries



# 用户登录认证接口

router_user=APIRouter(prefix="/api/v1",tags=["用户创建短链管理"])

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/api/v1/oauth2/authorize")

@router_user.post("/oauth2/authorize",summary="请求授权URL地址")
async def login(user_data:OAuth2PasswordRequestForm=Depends(),db_session:AsyncSession=Depends(get_db_session)):
    if not user_data:
        raise HTTPException(status_code=400,detail="请输入用户名和密码")
    # 查询用户是否存在
    userinfo=await UserServeries.get_user_by_name(db_session,user_data.username)
    if not userinfo:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="用户不存在",headers={"WWW-Authenticate":"Basic"})
    # 验证用户密码和哈希密码是否一致
    if not PasslibHelper.verify_password(user_data.password,userinfo.password):
        raise HTTPException(status_code=400,detail="用户密码不对")
    # 签发JWT有效负载信息
    data={
        'iss':userinfo.username,
        'sub':'xiaozhongtongxue',
        'username':userinfo.username,
        'admin':True,
        'exp':datetime.utcnow()+timedelta(minutes=30)
    }
    # 生成token
    token=AuthTokenHelper.token_encode(data=data)

    return {"access_token":token,"token_type":"bearer"}


@router_user.post("/create/single/short",summary="创建单一短链请求")
async def create_single(createinfo: SingShortUrlCreate, token: str, db_session: AsyncSession = Depends(get_db_session)):
    payload = AuthTokenHelper.decode_token(token)
    username = payload.get("username")
    createinfo.short_tag=generate_short_url()
    createinfo.short_url =f"{createinfo.short_url}{createinfo.short_url}"
    createinfo.created_by  = username
    createinfo.msg_context=f"{createinfo.msg_context},欲了解详情，请单击{createinfo.short_url} !"
    result=await ShortServeries.create_short_url(db_session,**createinfo.dict())
    return {"code":100,"msg":"创建短链成功","data":{"short_url":result.short_url}}

from fastapi import APIRouter,Depends,BackgroundTasks

from fastapi.responses import RedirectResponse,PlainTextResponse
from dependencies.dependencies import get_db_session
from db.database import AsyncSession
from servies.short import ShortServeries
from schemes.schemes import SingShortUrlCreate
from dependencies.dependencies import AuthTokenHelper



router_short=APIRouter(tags=["短链访问"])

@router_short.get("/{short_tag}")
async def short_redirect(*,short_tag:str,db_session:AsyncSession=Depends(get_db_session),tasks:BackgroundTasks):
    data=await ShortServeries.get_short_url(db_session,short_tag)
    if not data:
        return PlainTextResponse("没有对应的短链信息记录")
    data.visits_count+=1

    tasks.add_task(ShortServeries.update_short_url,db_session,short_url_id=data.id,visits_count=data.visits_count)
    return RedirectResponse(url=data.long_url)


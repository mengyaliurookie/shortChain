from pydantic import BaseModel


class SingShortUrlCreate(BaseModel):
    """
    创建新短链记录时需要传递参数信息
    """
    # 需要生成长链地址
    long_url:str
    # 短链生成前缀
    short_url:str="http://127.0.0.1:8000/"
    # 访问次数，默认值为0
    visits_count:int=0
    # 短链标签，默认值可以不传
    short_tag:str=""
    # 默认不传，通常在后端进行生成处理
    created_by:str=""


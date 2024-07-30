from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

# 라우터 생성
member_router = APIRouter()
# 템플릿 지정
templates = Jinja2Templates(directory='views/templates')

# 로그인 페이지
@member_router.get("/login", response_class=HTMLResponse)
async def login(req: Request):
    return templates.TemplateResponse('member/login.html',{'request':req})
# 회원가입 페이지
@member_router.get("/join", response_class=HTMLResponse)
async def join(req: Request):
    return templates.TemplateResponse('member/join.html',{'request':req})
# 내 정보 페이지
@member_router.get("/myinfo", response_class=HTMLResponse)
async def myinfo(req: Request):
    return templates.TemplateResponse('member/myinfo.html',{'request':req})
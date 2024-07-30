from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

# 라우터 생성
board_router = APIRouter()
# 템플릿 지정
templates = Jinja2Templates(directory='views/templates')

# 글쓰기 기능
@board_router.get("/write", response_class=HTMLResponse)
async def write(req: Request):
    return templates.TemplateResponse('board/write.html',{'request':req})
# 리스트 보기
@board_router.get("/list", response_class=HTMLResponse)
async def list(req: Request):
    return templates.TemplateResponse('board/list.html',{'request':req})
# 본문 보기
@board_router.get("/view", response_class=HTMLResponse)
async def view(req: Request):
    return templates.TemplateResponse('board/view.html',{'request':req})
# # 글 삭제
# @board_router.get("/remove", response_class=HTMLResponse)
# async def remove(req: Request):
#     return templates.TemplateResponse('board/remove.html',{'request':req})
# 글 수정
@board_router.get("/modify", response_class=HTMLResponse)
async def modify(req: Request):
    return templates.TemplateResponse('board/modify.html',{'request':req})
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRouter
from src.config.database import conn
from pymongo import MongoClient
from pathlib import Path
from bson import ObjectId
from src.config.settings import templates
from src.auth.schemas import USER_LOGIN,USER_REGISTER
from src.auth.service import handle_login, handle_signup
from fastapi import Query, Form
from pydantic import BaseModel
from typing import Annotated
from fastapi.responses import RedirectResponse
from src.auth.jwt import verify_token

router = APIRouter()

@router.get("/login", response_class=HTMLResponse)
async def login_url(request:Request):
  return templates.TemplateResponse(
    name="login.html",
    request=request,
    context={}
  )

@router.get("/signup", response_class=HTMLResponse)
async def signup_url(request: Request):
  if (user := await verify_token(request)) is not None:
    return RedirectResponse("/dashboard")
  return templates.TemplateResponse(
        name="signup.html",
        request=request,
        context={}
    )

@router.get("/auth", response_class=HTMLResponse)
async def auth_url(user : Annotated[USER_LOGIN,Query()],request:Request):
  return await handle_login(user,request)



@router.post("/register")
async def register_url(
    request: Request,
    first_name: str = Form(...),
    last_name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...)
):
    user = USER_REGISTER(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
    )
    return await handle_signup(user, request)



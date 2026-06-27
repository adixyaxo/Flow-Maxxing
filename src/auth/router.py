from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRouter
from src.config.database import conn
from pymongo import MongoClient
from pathlib import Path
from bson import ObjectId
from src.config.settings import templates
from src.auth.schemas import USER
from src.auth.service import handle_login, handle_signup
from fastapi import Query
from pydantic import BaseModel
from typing import Annotated

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
    return templates.TemplateResponse(
        name="signup.html",
        request=request,
        context={}
    )

@router.get("/auth", response_class=HTMLResponse)
async def login_url(user : Annotated[USER,Query()],request:Request):
  return handle_login(user,request)

@router.post("/register", response_class=HTMLResponse)
async def register_url(user:USER):
  return handle_signup(user)
from fastapi.templating import Jinja2Templates
from fastapi import Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRouter
from src.config.database import conn
from pymongo import MongoClient
from pathlib import Path
from bson import ObjectId
from src.config.settings import templates
from fastapi.security import OAuth2PasswordBearer
from src.auth.jwt import verify_token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

router = APIRouter()


@router.get("/profile", response_class=HTMLResponse)
async def profile_url(
    request: Request,
    current_user=Depends(verify_token)
):
    return templates.TemplateResponse(
        name="profile.html",
        request=request,
        context={"user":current_user}
    )


@router.get("/settings", response_class=HTMLResponse)
async def settings_url(
    request: Request,
    current_user=Depends(verify_token)
):
    return templates.TemplateResponse(
        name="settings.html",
        request=request,
        context={"user":current_user}
    )


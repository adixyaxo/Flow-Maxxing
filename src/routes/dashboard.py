from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRouter
from src.config.database import conn
from pymongo import MongoClient
from pathlib import Path
from bson import ObjectId
from src.config.settings import templates
from fastapi import Depends
from src.auth.jwt import verify_token
router = APIRouter()


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard_url(request: Request,current_user = Depends(verify_token)):
    return templates.TemplateResponse(
        name="dashboard.html",
        request=request,
        context={}
    )
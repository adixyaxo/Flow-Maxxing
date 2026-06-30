from src.user.schemas import USER
from src.config.database import conn
from src.config.settings import templates
from fastapi import Request

async def handle_profile(request: Request):
  return None
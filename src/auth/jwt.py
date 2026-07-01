import jwt
from src.auth.schemas import jwt_info
from src.config.environment import JWT_KEY, JWT_ALGO, JWT_EXP_TIME
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from src.config.database import users_DB
from fastapi.requests import Request
from bson import ObjectId


def generate_paylaod(_id:str,email:str,role:str):
  payload = {
    "_id":_id,
    "email":email,
    "role":role,
    "exp":datetime.now(timezone.utc) + timedelta(seconds=JWT_EXP_TIME)
  }
  return payload


def store_token(payload:dict):
  token = jwt.encode(payload,JWT_KEY,JWT_ALGO)
  return token


async def verify_token(request:Request):

  token = request.cookies.get("access_token")
  if token is None:
    raise HTTPException(status_code=307, headers={"Location": "/login"})

  try:
    payload = jwt.decode(
        token,
        JWT_KEY,
        algorithms=[JWT_ALGO]
    )
    user = await users_DB.find_one({
      "_id": ObjectId(payload["_id"])
    })
    if user is None:
            raise HTTPException(
                status_code=307,
                headers={"Location": "/login"}
            )
    return user
  except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=307,
            headers={"Location": "/login"}
        )

  except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=307,
            headers={"Location": "/login"}
        )
  except Exception as e:
    print("Unknown Exception Occurred")
    raise HTTPException(status_code=307, headers={"Location": "/login"})

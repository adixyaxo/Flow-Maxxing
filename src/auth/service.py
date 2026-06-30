from src.auth.schemas import USER_LOGIN,USER_REGISTER
from src.config.database import conn
from src.config.settings import templates
from src.config.environment import JWT_EXP_TIME
from fastapi import Request
from pymongo.errors import DuplicateKeyError
from src.auth.password import hash_password
from fastapi.responses import RedirectResponse
import bcrypt
from src.auth.jwt import verify_token,generate_paylaod,store_token
from datetime import datetime


async def handle_login(user: USER_LOGIN, request: Request):
  db_call = conn.users.find_one({
      "email": user.email
  })

  if db_call is None:
    return templates.TemplateResponse(
        "error.html",
        request=request,
        status_code=911,
        context={
            "code": 911,
            "title": "Wrong Credentials",
            "message": "Invalid email or password."
        }
    )

  try:
    if not bcrypt.checkpw((user.password).encode('utf-8'),(str(db_call.get("password"))).encode('utf-8')):
        return templates.TemplateResponse(
            name="error.html",
            request=request,
            context={
                "code": 911,
                "title": "Wrong Credentials",
                "message": "Sorry man either the email or the password is wrong"
            }
        )
    else:
        token = store_token(generate_paylaod(str(db_call.get("_id")),user.email,"USER"))
        response = RedirectResponse(url="/dashboard")
        response.set_cookie(
          key="access_token",
          value=token,
          httponly=True,
          secure=True,      # Use HTTPS
          samesite="Lax",
          max_age=JWT_EXP_TIME        # 15 minutes
        )
        return response
  except Exception as e:
        print(e)
        return templates.TemplateResponse(
            name="error.html",
            request=request,
            context={
              "code":"-1",
              "title":"Login Me Dikkat",
              "message":"Shyad Database me koi dikkat hai dekh kr batata hoon"
            }
        )


async def handle_signup(user:USER_REGISTER,request:Request):
  data = {
    "first_name":user.first_name,
    "last_name":user.last_name,
    "email":user.email,
    "password": hash_password(user.password).decode("utf-8")
  }

  try:
    conn.users.insert_one(data)
  except DuplicateKeyError:
    return templates.TemplateResponse(
      name="error.html",
      request=request,
      context={
        "code":911,
        "title":"FAM! User already exits",
        "message":"Damn! man like Damn! there is already an account here with this email try with something else man"
      }
    )
  response = RedirectResponse(url="/dashboard",status_code=303)
  return response
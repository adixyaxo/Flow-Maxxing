from src.auth.schemas import USER
from src.config.database import conn
from src.config.settings import templates
from fastapi import Request


def handle_login(user:USER,request:Request):
  print(user)
  existing = conn.users.find_one({"email":user.email,"password":user.password})
  print(existing)
  if not(existing):
    return templates.TemplateResponse(
      name="error.html",
      request=request,
      context={
        "code":911,
        "title":"Wrong Credentials",
        "message":"Sorry man either the email or the password is wrong"

      }
    )
  else:
    return templates.TemplateResponse(
      name="message.html",
      request=request,
      context={"code":"001",
              "title":"Sign In Successfull",
              "message":"The signup process for a major success"}
  )


def handle_signup(user:USER,request:Request):
  print(user)
  existing = conn.users.find_one({"email":user.email})
  print(existing)
  if existing:
    return templates.TemplateResponse(
      name="error.html",
      request=request,
      context={
        "code":911,
        "title":"FAM! User already exits",
        "message":"Damn! man like Damn! there is already an account here with this email try with something else man"

      }
    )
  else:
    return templates.TemplateResponse(
      name="message.html",
      request=request,
      context={"code":"001",
              "title":"Sign Up Successfull",
              "message":"The signup process for a major success"}
  )
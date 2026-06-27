from pydantic import BaseModel , EmailStr

class USER(BaseModel):
  email:str
  password:str
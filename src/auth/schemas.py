from pydantic import BaseModel

class USER_LOGIN(BaseModel):
    email: str
    password: str

class USER_REGISTER(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class jwt_info(BaseModel):
    _id:str
    email:str
    role:str
    exp:str

class Token(BaseModel):
    access_token: str
    token_type: str
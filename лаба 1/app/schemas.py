
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    full_name: str | None = None
    password: str

class UserUpdate(BaseModel):
    username: str | None = None
    email: str | None = None
    full_name: str | None = None
    password: str | None = None
    disabled: bool | None = None

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    full_name: str | None = None
    disabled: bool | None = None

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    refresh_token: str | None = None
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from src.auth.models import Permission

class UserBase(BaseModel):
    email: EmailStr
    username: str
    first_name: str
    last_name: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    username: str | None
    email: EmailStr | None
    first_name: str | None
    last_name: str | None

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class PermissionBase(BaseModel):
    name: str
    description: str

class PermissionCreate(PermissionBase):
    pass

class PermissionUpdate(PermissionBase):
    name: str | None
    description: str | None

class PermissionOut(PermissionBase):
    id: int

    class Config:
        orm_mode = True

class GroupBase(BaseModel):
    name: str
    description: str
    permissions: list[int] = []

class GroupCreate(GroupBase):
    pass

class GroupUpdate(GroupBase):
    name: str | None
    description: str | None
    permissions: list[int] | None

class GroupOut(GroupBase):
    id: int

    class Config:
        orm_mode = True

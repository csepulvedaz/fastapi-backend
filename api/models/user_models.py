from pydantic import BaseModel, EmailStr
from enum import Enum
from uuid import UUID
from typing import Optional


class Role(str, Enum):
    admin = "admin"
    user = "user"


class UserCreate(BaseModel):
    role: Role = Role.user
    email: EmailStr
    name: str
    last_name: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "role": "user",
                "email": "john@example.com",
                "name": "jhon",
                "last_name": "doe",
                "password": "password",
            }
        }


class UserUpdate(BaseModel):
    email: Optional[EmailStr]
    name: Optional[str]
    last_name: Optional[str]
    password: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "email": "john@example.com",
                "name": "jhon",
                "last_name": "doe",
                "password": "password",
            }
        }


class User(BaseModel):
    id: UUID
    role: Role
    email: EmailStr
    name: str
    last_name: str

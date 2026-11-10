from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]] = []

    class Config:
        schema_extra = {
            "example": {
                "email": "GodchaGotchs@gavmail.com",
                "username": "password123",
                "events": [],
            }
        }

class NewUser(User):
    username: str

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "GodchaGotchs@gavmail.com",
                "username": "password123",
                "events": [],
            }
        }
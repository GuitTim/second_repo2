from typing import List, Optional
from beanie import Document
from pydantic import BaseModel


class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Презентация книги по FastAPI",
                "image": "https://linktomyimage.com/image.png",
                "description": "На встрече обсудим содержание книги по FastAPI. Приходите со своим экземпляром, чтобы поучаствовать в розыгрыше!",
                "tags": ["python", "fastapi", "книга", "презентация"],
                "location": "Google Meet",
            }
        }

    class Settings:
        name = "events"


class EventUpdate(BaseModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Обновлённое название события",
                "image": "https://linktomyimage.com/image.png",
                "description": "Обновлённое описание события",
                "tags": ["python", "fastapi"],
                "location": "Гибрид",
            }
        }
from typing import List, Optional
from pydantic import BaseModel

class Todo(BaseModel):
    id: Optional[int] = None
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "item": "Завершить работу (Аюпов Т.М.)"
            }
        }

class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "item": "zpf,skxnjnen (Аюпов Т.М.)"
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {"item": "Задача 1 (Аюпов Т.М.)"},
                    {"item": "Задача 2 (Аюпов Т.М.)"}
                ]
            }
        }
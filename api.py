from fastapi import FastAPI
from todo import todo_router

app = FastAPI(title="Веб-приложение задач студента Аюпова Т.М.")

@app.get("/")
async def welcome() -> dict:
    return {
        "message": "FastAPI с шаблонами Jinja2 (Аюпов Т.М.)"
    }

app.include_router(todo_router)
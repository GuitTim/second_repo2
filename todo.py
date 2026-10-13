from fastapi import APIRouter, Path, HTTPException, status, Request
from fastapi.templating import Jinja2Templates
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()
todo_list = []

templates = Jinja2Templates(directory="templates/")

@todo_router.post("/todo")
async def add_todo(request: Request):
    form_data = await request.form()
    item_text = form_data.get("item")
    
    if item_text:
        new_todo = Todo(id=len(todo_list) + 1, item=item_text)
        todo_list.append(new_todo)
        
    return templates.TemplateResponse(
        request, 
        "todo.html", 
        {
            "todos": todo_list
        }
    )

@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo(request: Request):
    return templates.TemplateResponse(
        request, 
        "todo.html", 
        {
            "todos": todo_list
        }
    )

@todo_router.get("/todo/{todo_id}")
async def get_single_todo(
    request: Request, 
    todo_id: int = Path(..., title="ID задачи для получения")
):
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse(
                request, 
                "todo.html", 
                {
                    "todo": todo
                }
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Нет задачи с указанным ID (Аюпов Т.М.)"
    )
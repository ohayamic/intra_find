from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from model import Todo, SignUp
from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo,
    fetch_one_signUp,
    fetch_all_signUps,
    create_signUp,
    update_signUp,
    remove_signUp,
)

# an HTTP-specific exception class  to generate exception information

app = FastAPI()
origins = ["http://localhost:3000"]

# what is a middleware? 
# software that acts as a bridge between an operating system or database and applications, especially on a network.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/todo", tags=['Todo'])
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get("/api/todo/{title}", tags=['Todo'], response_model=Todo)
async def get_todo_by_title(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")

@app.post("/api/todo/", tags=['Todo'], response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.put("/api/todo/{title}/", tags=['Todo'], response_model=Todo)
async def put_todo(title: str, desc: str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")

@app.delete("/api/todo/{title}", tags=['Todo'],)
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the title {title}")

@app.get("/api/signUp", tags=['SignUp'])
async def get_signUp():
    response = await fetch_all_signUps()
    return response

@app.get("/api/signUp/{firstname}", tags=['SignUp'], response_model=SignUp)
async def get_signUp_by_firstname(firstname):
    response = await fetch_one_signUp(firstname)
    if response:
        return response
    raise HTTPException(404, f"There is no signUp with the firstname {firstname}")

@app.post("/api/signUp/", tags=['SignUp'], response_model=SignUp)
async def post_signUp(signUp: SignUp):
    response = await create_signUp(signUp.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.put("/api/signUp/{firstname}/", tags=['SignUp'], response_model=SignUp)
async def put_signUp(firstname: str, signup: SignUp):
    print(signup.dict())
    response = await update_signUp(firstname, signup)
    if response:
        return response
    raise HTTPException(404, f"There is no signUp with the firstname {firstname}")

@app.delete("/api/signUp/{firstname}", tags=['SignUp'])
async def delete_signUp(firstname):
    response = await remove_signUp(firstname)
    if response:
        return "Successfully deleted signUp"
    raise HTTPException(404, f"There is no signUp with the firstname {firstname}")
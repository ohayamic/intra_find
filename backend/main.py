from fastapi import FastAPI, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from model import Todo, SignUp, UpdateSignUp
from database import (
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

@app.put("/api/signUp/{lastname}", tags=['SignUp'], response_model=UpdateSignUp)
async def put_signUp(lastname: str, signup: UpdateSignUp = Body(...)):
    signup = {k: v for k, v in signup.dict().items() if v is not None}
    if len(signup)>=1:
        response = await update_signUp(lastname, signup)
    if response:
        return response
    raise HTTPException(404, f"There is no signUp with the lastname {lastname}")

@app.delete("/api/signUp/{firstname}", tags=['SignUp'])
async def delete_signUp(firstname):
    response = await remove_signUp(firstname)
    if response:
        return "Successfully deleted signUp"
    raise HTTPException(404, f"There is no signUp with the firstname {firstname}")
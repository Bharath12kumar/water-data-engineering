from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,Field

app=FastAPI()

user_details ={}
count_id=1

class user(BaseModel):
    name: str=Field(...,min_length=3,max_length=20)
    phone: int=Field(...,ge=999999999,le=10000000000)
    email:str

@app.post('/create')
def create_user(user:user):
    global count_id
    user_details[count_id]=user
    response ={
        "message":"user successfully Created",
        "user_id" : count_id,
        "user": user_details[count_id]
    }
    count_id += 1
    return response

@app.get('/users')
def get_users():
    if not user_details:
        raise HTTPException(status_code=404,details="no user found")
    return user_details

@app.get('/user/{user_id}')
def get_single_users(user_id:int):
    if user_id not in user_details:
        raise HTTPException(status_code=404,detail="No user found")
    return user_details[user_id]
    
@app.put('/user/{user_id}')
def update_user(user_id:int,user:user):
    if user_id not in user_details:
        raise HTTPException(status_code=404,detail="No user found")
    user_details[user_id]=user
    return {"message":"user updated ","user":user}

@app.delete('/user/{user_id}')
def delete_user(user_id:int):
    if user_id not in user_details:
        raise HTTPException(status_code=404,detail="No user found")
    delete =user_details.pop(user_id)
    return {"message":"user deleted ","user":delete}
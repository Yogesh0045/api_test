from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_db = {

    1: {"name" : "Yogesh", "age": 36},
    2: {"name": "Ishan", "age": 8},
    3: {"name": "Yashika", "age":9}
}

class User(BaseModel):
    name: str
    age: int

@app.put("/user_id/data/v1/update/{user_id}")
def user_update(user_id:int, user:User):
    if user_id in user_db:
        user_db[user_id]= user.dict()
        print(user_db)
        return {"message": "User updated successfully", "User": user_db[user_id]}
    
    else:
        return {"message": "User not found"}
    

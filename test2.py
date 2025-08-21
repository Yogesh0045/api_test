from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get("/yogesh")
def add(a:int, b:int):
    return (a + b)

print(add(3, 3))

class substractmodel(BaseModel):
    a : int
    b : int


def substract(a:int, b:int):
    return (a - b)

@app.post("/substract")
def substarct_numbers(model:substractmodel):
    return (model.a, model.b)

print(substract(6, 3))
 
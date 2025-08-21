from fastapi import FastAPI

app = FastAPI()

@app.get("/yogesh/kumar")
def add(a:int, b:int):
    return (a + b)

print(add(3, 3))

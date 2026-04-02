from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/greet")
async def greet():
    return [{"name": "Hello, pragyan!"},
            {"name": "Welcome to DataScience!"}]


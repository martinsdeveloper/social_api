
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
import uvicorn

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route
@app.get("/")
def read_root():
    return {"message": "Hello, World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
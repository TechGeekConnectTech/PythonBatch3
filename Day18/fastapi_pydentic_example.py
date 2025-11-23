from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from pydantic import BaseModel


class Student(BaseModel):
    name:str
    age:int
    phone:str
    course:str



app = FastAPI()

@app.post("/add_student")
def add_student(student: Student):
   return JSONResponse(content={"message":"Student added successfully"}, status_code=201)
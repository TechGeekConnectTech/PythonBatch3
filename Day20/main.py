from fastapi import FastAPI, HTTPException, Header, Query, Depends
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from db import database
from validate_token import check_token
import json
    

app = FastAPI(dependencies=[Depends(check_token.verify_token), Depends(database.setup_db)])
class Student(BaseModel):
    student_id:int
    student_name:str
    student_age:int
    student_marks:int

@app.get("/students")
def get_students(db=Depends(database.get_db)):
       
    if db:
        return JSONResponse(content=db, status_code=200,headers={"version":"1.1.0"})
    else:
        raise HTTPException(status_code=404, detail="No data found")
    

#query parameter
@app.get("/students/marks")
def get_students_marks(marks: int= Query(...),age: int= Query(...),
                       db=Depends(database.get_db)):
    student_list=[]
    for student in db:
        if student['student_marks']>=marks and student['student_age']>=age:
            student_list.append(student)
    
    if student_list:
        return JSONResponse(content=student_list, status_code=200,headers={"version":"1.1.0"})
    else:
        raise HTTPException(status_code=404, detail="No data found")


@app.post("/students")
def add_student(student:Student,
                db=Depends(database.get_db)):    
    
    for stud in db:
        if stud['student_id']==student.student_id:
            raise HTTPException(status_code=400, detail="Student with given ID already exists")
        
    db.append(student.dict())
    database.write_db(db)
    return JSONResponse(content={"message":"Student added successfully"}, status_code=201,headers={"version":"1.1.0"})
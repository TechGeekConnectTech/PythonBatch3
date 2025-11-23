from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
app = FastAPI()

@app.get("/student_info")
def student_info():
    data = [{
        "name": "Rajesh Borkar",
        "age":20,
        "course":"B.Tech",
        "branch":"Computer Science"
    },
    {
        "name": "Suresh Jadhav",
        "age":22,
        "course":"B.Tech",
        "branch":"Mechanical"
    }]
    return JSONResponse(content=data, status_code=200)


@app.get("/student_info/{student_id}")
def student_info(student_id: int):
    data = [{
        "id": 1,
        "name": "Rajesh Borkar",
        "age":20,
        "course":"B.Tech",
        "branch":"Computer Science"
    },
    {
        "id": 2,
        "name": "Suresh Jadhav",
        "age":22,
        "course":"B.Tech",
        "branch":"Mechanical"
    }]
    for student in data:
        if student["id"] == student_id:
            return JSONResponse(content=student, status_code=200)
    
    raise HTTPException(status_code=404, detail="Student not found")



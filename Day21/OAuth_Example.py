from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
import json

app = FastAPI()
SECRET_KEY = "p8Xw!7zQ2rT#v9LmS4eY@1bN6uJ$k5HcG0fVxZ3tWqE8sRjD"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
fake_users_db = {
    "username":"testuser",
    "password":"testpass"
}

def create_access_token(data: dict):
    to_encode = data.copy()
    print(to_encode)
    expiry = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expiry})
    token=jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != fake_users_db["username"] or form_data.password != fake_users_db["password"]:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token= create_access_token({"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    
@app.get("/getuser") 
def get_user(current_user: str = Depends(get_current_user)):
    return JSONResponse(content={"username": current_user}, status_code=200)


@app.get("/students")
def get_students(current_user: str = Depends(get_current_user)):
    if current_user:       
        with open("students.json", "r") as f:
            data = f.read()
            students = json.loads(data)
            return JSONResponse(content=students, status_code=200)
    else:
        raise HTTPException(status_code=404, detail="No data found")
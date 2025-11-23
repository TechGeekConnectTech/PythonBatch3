from fastapi import FastAPI, Response
app = FastAPI()

@app.get("/show_hello")
def show_hello(response: Response):
   response.status_code=200
   return {"message":"Hello World from FastAPI"}




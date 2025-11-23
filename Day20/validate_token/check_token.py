from fastapi import Header, HTTPException
def verify_token(x_api_key: str = Header(...)):
    if x_api_key != "mysecretkey":
        raise HTTPException(status_code=401, detail="Unauthorized")
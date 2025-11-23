from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import json


app = FastAPI()

File_Name="product.json"

def read_product():
    with open(File_Name,'r') as f:
        return json.load(f)
    
def write_product(data):
    with open(File_Name,'w') as f:
        json.dump(data,f,indent=4)    

class Product(BaseModel):
    product_name: str
    product_model: str
    product_price: int
    product_quantity: int


# CRUD Operations
# Get all products 
@app.get("/")
def get_root():
    return {"message":"Welcome to Product Management API"}

@app.get("/products")
def get_all_products():
    products=read_product()
    if not products:
        raise HTTPException(status_code=404,detail="No products found")
    return JSONResponse(content=products,status_code=200)

@app.get("/products/{product_name}")
def get_product_by_name(product_name: str):
    products=read_product()
    product_list=[]
    for product in products:
        if product["product_name"]==product_name:
            product_list.append(product)
    
    if product_list:
        return JSONResponse(content=product_list,status_code=200)
    
    raise HTTPException(status_code=404,detail="Product not found")


# Post a product
@app.post("/product")
def add_product(product:Product):
    products=read_product()
    for p in products:
        if p["product_name"]==product.product_name and p["product_model"]==product.product_model:
            raise HTTPException(status_code=400,detail="Product already exists")
    products.append(product.dict())
    write_product(products)
    return JSONResponse(content={"message":"Product added successfully"},status_code=201)

@app.delete("/product/{product_name}/{product_model}")
def delete_product(product_name:str, product_model:str):
    products=read_product()
    for product in products:
        if product["product_name"]==product_name and product["product_model"]==product_model:
            products.remove(product)
            write_product(products)
            return JSONResponse(content={"message":"Product deleted successfully"},status_code=200)
        
    raise HTTPException(status_code=404,detail="Product not found")

@app.patch("/product/{product_name}/{product_model}/quantity/{quantity}")
def update_product_quantity(product_name:str, product_model:str, quantity:int):
    products=read_product()
    for product in products:
        if product["product_name"]==product_name and product["product_model"]==product_model:
            exist_quantity = product["product_quantity"]
            if quantity > exist_quantity:
                raise HTTPException(status_code=400,detail="Insufficient product quantity")
            product["product_quantity"]=exist_quantity - quantity
            write_product(products)
            return JSONResponse(content={"message":"Product quantity updated successfully"},status_code=200)
        
    raise HTTPException(status_code=404,detail="Product not found")

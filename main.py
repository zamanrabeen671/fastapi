from fastapi import FastAPI
from models import Product
from database import SessionLocal, engine
import database_models

app = FastAPI()
database_models.Base.metadata.create_all(bind=engine)

@app.get('/')
def greeter():
    return "Hello its me"

products = [
    Product(id = 1, name = "mobile xp", description= "this is smartphone", price = 100.11,  quantity=2),
    Product(id = 2, name = "mobile bp", description= "this is smartphone", price = 100.11,  quantity=2),
    Product(id = 3, name = "mobile cp", description= "this is smartphone", price = 100.11,  quantity=2),
    Product(id = 4, name = "mobile cp", description= "this is smartphone", price = 100.11,  quantity=2),
]

@app.get('/products')
def product():
    db = SessionLocal()
    db.query()
    return products

@app.get('/product/{id}')
def singleProduct(id: int):
    for product in products:
        if product.id == id:
            return product
    
    return "Not Found"

@app.post('/product')
def add_product(product: Product):
    products.append(product)
    
    return product
from fastapi import FastAPI,  Depends, HTTPException
from models import Product
from database import SessionLocal, engine
import database_models
from sqlalchemy.orm import Session
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

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def _init_db():
    db = SessionLocal()

    existing_count = db.query(database_models.Product).count()

    if existing_count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()
        print("Database initialized with sample products.")
        
    db.close()
_init_db()

@app.get("/products/")
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(database_models.Product).all()
    return products

@app.get("/products/{product_id}")
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
    if product:
        return product
    return {"error": "Product not found"}

@app.post("/products/")
def create_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return {"message": "Product created successfully", "product": product}

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.quantity = product.quantity
    db.commit()
    db.refresh(db_product)
    return {"message": "Product updated successfully", "product": db_product}


@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}
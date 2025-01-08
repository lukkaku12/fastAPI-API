from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.db import get_db
from DTOs.product_dto import CreateProduct
from services.product_service import (
    list_products_service,
    retrieve_product_service,
    create_product_service,
    delete_product_service,
)

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/")
def list_products(db: Session = Depends(get_db)):
    try:
        return list_products_service(db)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{id}")
def retrieve_product(id: int, db: Session = Depends(get_db)):
    try:
        return retrieve_product_service(db, id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", status_code=201)
def create_product(product: CreateProduct, db: Session = Depends(get_db)):
    try:
        return create_product_service(db, product)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{id}")
def remove_product(id: int, db: Session = Depends(get_db)):
    try:
        delete_product_service(db, id)
        return {"detail": "Producto eliminado con éxito."}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
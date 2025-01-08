from sqlalchemy.orm import Session
from typing import List, Optional
from DTOs.product_dto import CreateProduct
from app.repository.product_repository import (
    get_products,
    get_product,
    create_product,
    delete_product,
)
from app.models.model import Product


def list_products_service(db: Session) -> List[Product]:
    """
    Servicio para listar todos los productos.
    """
    products = get_products(db)
    if not products:
        raise ValueError("No hay productos disponibles.")
    return products


def retrieve_product_service(db: Session, id: int) -> Optional[Product]:
    """
    Servicio para obtener un producto por ID.
    """
    product = get_product(db, id)
    if not product:
        raise ValueError(f"No se encontró un producto con ID {id}.")
    return product


def create_product_service(db: Session, product: CreateProduct) -> Product:
    """
    Servicio para crear un nuevo producto con validaciones básicas.
    """
    if not product.name or len(product.name) < 3:
        raise ValueError("El nombre del producto debe tener al menos 3 caracteres.")
    if product.stock < 0:
        raise ValueError("El stock no puede ser negativo.")
    if product.price <= 0:
        raise ValueError("El precio debe ser mayor a 0.")

    new_product = create_product(db, product)
    if not new_product:
        raise ValueError("No se pudo crear el producto.")
    return new_product


def delete_product_service(db: Session, id: int) -> None:
    """
    Servicio para eliminar un producto por ID.
    """
    product = get_product(db, id)
    if not product:
        raise ValueError(f"No se encontró un producto con ID {id} para eliminar.")

    delete_product(db, id)
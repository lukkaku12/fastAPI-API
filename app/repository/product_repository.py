from models.model import Product 
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from typing import Optional
from DTOs.product_dto import CreateProduct


def get_products(db: Session) -> any:
    """Obtiene todos los productos de la base de datos."""
    return db.query(Product).all()  # Usar `Product`, no `products`


def get_product(db: Session, id: int) -> Optional[Product]:
    """Obtiene un producto por su ID."""
    try:
        return db.query(Product).filter(Product.id == id).one()  # Usar `Product`
    except NoResultFound:
        return None


def create_product(db: Session, product: CreateProduct) -> Optional[Product]:
    """Crea un nuevo producto en la base de datos."""
    db_product = Product(  # Usar `Product`
        name=product.name,
        description=product.description,
        stock=product.stock,
        price=product.price,
    )

    db.add(db_product)

    try:
        db.commit()
        db.refresh(db_product)
        return db_product
    except Exception as e:
        db.rollback()
        print(f"Error al crear el producto: {e}")
        return None


def delete_product(db: Session, id: int) -> bool:
    """Elimina un producto por su ID."""
    product = db.query(Product).filter(Product.id == id).first()  # Usar `Product`
    if product:
        db.delete(product)
        db.commit()
        return True
    return False
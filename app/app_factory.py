from fastapi import FastAPI
from app.routes.product_routes import router
from models.db import engine, Base 
from models.model import Product

class AppFactory:
    @staticmethod
    def create_app() -> FastAPI:

        
        # Base.metadata.drop_all(bind=engine)
        
        Base.metadata.create_all(bind=engine)

        app = FastAPI()

        # Registrar rutas
        app.include_router(router)

        # Agregar middlewares o configuraciones adicionales si es necesario
        # app.add_middleware(...)

        return app
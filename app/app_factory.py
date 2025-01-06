from fastapi import FastAPI
from app.routes import router  # Importa tus rutas
from models.db import engine, Base 

class AppFactory:
    @staticmethod
    def create_app() -> FastAPI:
        
        Base.metadata.create_all(bind=engine)

        app = FastAPI()

        # Registrar rutas
        app.include_router(router)

        # Agregar middlewares o configuraciones adicionales si es necesario
        # app.add_middleware(...)

        return app
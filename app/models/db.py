from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

# URL de conexión a PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://miusuario:micontraseña@localhost:5432/mibase"

# Crear un motor de base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Crear la clase base para los modelos
Base = declarative_base()

# Crear una fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

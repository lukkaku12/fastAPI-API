from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

# URL de conexión a PostgreSQL
# SQLALCHEMY_DATABASE_URL = "postgresql://miusuario:micontraseña@192.168.1.8:5432/mibase"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:your_password@localhost:5432/your_database"

# Crear un motor de base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Crear la clase base para los modelos
Base = declarative_base()

# Crear una fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# session = SessionLocal()

# session.close()

# Dependencia para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
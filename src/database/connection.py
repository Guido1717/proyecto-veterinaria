"""Configuración de la conexión a PostgreSQL (Neon) con SQLAlchemy."""
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError(
        "Falta la variable DATABASE_URL. Créala en el archivo .env "
        "(ver README.md)."
    )

# pool_pre_ping revisa la conexión antes de usarla: Neon cierra las
# conexiones inactivas y sin esto la primera petición fallaría.
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_session():
    """Devuelve una sesión nueva. Quien la usa debe cerrarla."""
    return SessionLocal()

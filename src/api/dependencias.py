"""Dependencias compartidas por los routers."""
from collections.abc import Iterator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from src.database.connection import SessionLocal


def obtener_db() -> Iterator[Session]:
    """Abre una sesión por petición y la cierra al terminar."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


SesionDB = Annotated[Session, Depends(obtener_db)]

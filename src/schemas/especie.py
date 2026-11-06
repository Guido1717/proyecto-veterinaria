"""Schemas de la entidad Especie."""
from pydantic import Field

from src.schemas.base import ActualizacionBase, CreacionBase, LecturaBase


class EspecieCreate(CreacionBase):
    nombre: str = Field(min_length=1, max_length=50, examples=["Canino"])
    descripcion: str = Field(
        default="", max_length=200, examples=["Perros de cualquier raza"]
    )


class EspecieUpdate(ActualizacionBase):
    nombre: str | None = Field(default=None, min_length=1, max_length=50)
    descripcion: str | None = Field(default=None, max_length=200)


class EspecieRead(LecturaBase):
    nombre: str
    descripcion: str | None

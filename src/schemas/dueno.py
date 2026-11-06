"""Schemas de la entidad Dueno."""
from pydantic import Field

from src.schemas.base import ActualizacionBase, CreacionBase, LecturaBase


class DuenoCreate(CreacionBase):
    nombre: str = Field(min_length=1, max_length=100, examples=["Ana Gómez"])
    telefono: str = Field(min_length=1, max_length=20, examples=["3109876543"])
    direccion: str = Field(
        default="", max_length=200, examples=["Carrera 15 #8-30"]
    )


class DuenoUpdate(ActualizacionBase):
    nombre: str | None = Field(default=None, min_length=1, max_length=100)
    telefono: str | None = Field(default=None, min_length=1, max_length=20)
    direccion: str | None = Field(default=None, max_length=200)


class DuenoRead(LecturaBase):
    nombre: str
    telefono: str
    direccion: str | None

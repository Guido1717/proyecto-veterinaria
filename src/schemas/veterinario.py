"""Schemas de la entidad Veterinario."""
from pydantic import Field

from src.schemas.base import ActualizacionBase, CreacionBase, LecturaBase


class VeterinarioCreate(CreacionBase):
    nombre: str = Field(
        min_length=1, max_length=100, examples=["Laura Torres"]
    )
    especialidad: str = Field(
        min_length=1, max_length=100, examples=["Medicina general"]
    )
    telefono: str = Field(min_length=1, max_length=20, examples=["3201112233"])


class VeterinarioUpdate(ActualizacionBase):
    nombre: str | None = Field(default=None, min_length=1, max_length=100)
    especialidad: str | None = Field(
        default=None, min_length=1, max_length=100
    )
    telefono: str | None = Field(default=None, min_length=1, max_length=20)


class VeterinarioRead(LecturaBase):
    nombre: str
    especialidad: str
    telefono: str

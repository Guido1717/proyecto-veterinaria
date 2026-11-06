"""Schemas de la entidad Mascota."""
from pydantic import Field

from src.schemas.base import ActualizacionBase, CreacionBase, LecturaBase


class MascotaCreate(CreacionBase):
    nombre: str = Field(min_length=1, max_length=50, examples=["Rocky"])
    edad: int = Field(ge=0, examples=[3])
    especie_id: int = Field(gt=0, examples=[1])
    dueno_id: int = Field(gt=0, examples=[1])


class MascotaUpdate(ActualizacionBase):
    nombre: str | None = Field(default=None, min_length=1, max_length=50)
    edad: int | None = Field(default=None, ge=0)
    especie_id: int | None = Field(default=None, gt=0)
    dueno_id: int | None = Field(default=None, gt=0)


class MascotaRead(LecturaBase):
    nombre: str
    edad: int
    especie_id: int
    dueno_id: int

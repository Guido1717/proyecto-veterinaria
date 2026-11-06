"""Schemas de la entidad Vacuna."""
from datetime import date

from pydantic import Field

from src.schemas.base import ActualizacionBase, CreacionBase, LecturaBase


class VacunaCreate(CreacionBase):
    nombre: str = Field(min_length=1, max_length=100, examples=["Rabia"])
    fecha_aplicacion: date = Field(examples=["2026-08-15"])
    mascota_id: int = Field(gt=0, examples=[1])


class VacunaUpdate(ActualizacionBase):
    nombre: str | None = Field(default=None, min_length=1, max_length=100)
    fecha_aplicacion: date | None = None
    mascota_id: int | None = Field(default=None, gt=0)


class VacunaRead(LecturaBase):
    nombre: str
    fecha_aplicacion: date
    mascota_id: int

"""Schemas de la entidad Cita."""
from datetime import date
from typing import Literal

from pydantic import Field

from src.schemas.base import ActualizacionBase, CreacionBase, LecturaBase

EstadoCita = Literal["pendiente", "atendida", "cancelada"]


class CitaCreate(CreacionBase):
    fecha: date = Field(examples=["2026-09-15"])
    estado: EstadoCita = "pendiente"
    mascota_id: int = Field(gt=0, examples=[1])
    veterinario_id: int = Field(gt=0, examples=[1])


class CitaUpdate(ActualizacionBase):
    fecha: date | None = None
    estado: EstadoCita | None = None
    mascota_id: int | None = Field(default=None, gt=0)
    veterinario_id: int | None = Field(default=None, gt=0)


class CitaRead(LecturaBase):
    fecha: date
    estado: str
    mascota_id: int
    veterinario_id: int

"""Schemas de la entidad Tratamiento."""
from pydantic import Field

from src.schemas.base import ActualizacionBase, CreacionBase, LecturaBase


class TratamientoCreate(CreacionBase):
    medicamento: str = Field(
        min_length=1, max_length=100, examples=["Antiemético"]
    )
    duracion_dias: int = Field(ge=1, examples=[5])
    consulta_id: int = Field(gt=0, examples=[1])


class TratamientoUpdate(ActualizacionBase):
    medicamento: str | None = Field(default=None, min_length=1, max_length=100)
    duracion_dias: int | None = Field(default=None, ge=1)
    consulta_id: int | None = Field(default=None, gt=0)


class TratamientoRead(LecturaBase):
    medicamento: str
    duracion_dias: int
    consulta_id: int

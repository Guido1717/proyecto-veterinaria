"""Schemas de la entidad Consulta."""
from pydantic import Field

from src.schemas.base import ActualizacionBase, CreacionBase, LecturaBase


class ConsultaCreate(CreacionBase):
    diagnostico: str = Field(
        min_length=1, max_length=300, examples=["Chequeo general, todo normal"]
    )
    observaciones: str = Field(
        default="", max_length=300, examples=["Peso adecuado"]
    )
    cita_id: int = Field(gt=0, examples=[1])


class ConsultaUpdate(ActualizacionBase):
    """La cita de una consulta no se cambia: se elimina y se crea otra."""

    diagnostico: str | None = Field(default=None, min_length=1, max_length=300)
    observaciones: str | None = Field(default=None, max_length=300)


class ConsultaRead(LecturaBase):
    diagnostico: str
    observaciones: str | None
    cita_id: int

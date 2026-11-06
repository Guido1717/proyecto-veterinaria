"""Operaciones CRUD de la entidad Tratamiento."""
from sqlalchemy.orm import Session

from src.crud.base import (
    aplicar_cambios,
    eliminar,
    guardar,
    listar,
    obtener_o_error,
    validar_referencia,
)
from src.database.models import Consulta, Tratamiento
from src.schemas.tratamiento import TratamientoCreate, TratamientoUpdate

ENTIDAD = "El tratamiento"


def _validar_referencias(db: Session, cambios: dict) -> None:
    if "consulta_id" in cambios:
        validar_referencia(
            db, Consulta, cambios["consulta_id"], "La consulta"
        )


def crear_tratamiento(db: Session, datos: TratamientoCreate) -> Tratamiento:
    valores = datos.model_dump()
    _validar_referencias(db, valores)
    return guardar(db, Tratamiento(**valores))


def listar_tratamientos(db: Session) -> list[Tratamiento]:
    return listar(db, Tratamiento)


def obtener_tratamiento(db: Session, tratamiento_id: int) -> Tratamiento:
    return obtener_o_error(db, Tratamiento, tratamiento_id, ENTIDAD)


def actualizar_tratamiento(
    db: Session, tratamiento_id: int, datos: TratamientoUpdate
) -> Tratamiento:
    tratamiento = obtener_tratamiento(db, tratamiento_id)
    cambios = datos.model_dump(exclude_unset=True)
    _validar_referencias(db, cambios)
    aplicar_cambios(tratamiento, cambios)
    return guardar(db, tratamiento)


def eliminar_tratamiento(db: Session, tratamiento_id: int) -> None:
    eliminar(db, obtener_tratamiento(db, tratamiento_id), {})

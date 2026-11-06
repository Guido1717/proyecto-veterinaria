"""Operaciones CRUD de la entidad Especie."""
from sqlalchemy.orm import Session

from src.crud.base import (
    aplicar_cambios,
    eliminar,
    guardar,
    listar,
    obtener_o_error,
)
from src.database.models import Especie
from src.schemas.especie import EspecieCreate, EspecieUpdate

ENTIDAD = "La especie"


def crear_especie(db: Session, datos: EspecieCreate) -> Especie:
    return guardar(db, Especie(**datos.model_dump()))


def listar_especies(db: Session) -> list[Especie]:
    return listar(db, Especie)


def obtener_especie(db: Session, especie_id: int) -> Especie:
    return obtener_o_error(db, Especie, especie_id, ENTIDAD)


def actualizar_especie(
    db: Session, especie_id: int, datos: EspecieUpdate
) -> Especie:
    especie = obtener_especie(db, especie_id)
    aplicar_cambios(especie, datos.model_dump(exclude_unset=True))
    return guardar(db, especie)


def eliminar_especie(db: Session, especie_id: int) -> None:
    especie = obtener_especie(db, especie_id)
    eliminar(db, especie, {
        "mascotas": "No se puede eliminar la especie porque tiene "
                    "mascotas asociadas",
    })

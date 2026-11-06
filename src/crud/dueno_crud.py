"""Operaciones CRUD de la entidad Dueno."""
from sqlalchemy.orm import Session

from src.crud.base import (
    aplicar_cambios,
    eliminar,
    guardar,
    listar,
    obtener_o_error,
)
from src.database.models import Dueno
from src.schemas.dueno import DuenoCreate, DuenoUpdate

ENTIDAD = "El dueño"


def crear_dueno(db: Session, datos: DuenoCreate) -> Dueno:
    return guardar(db, Dueno(**datos.model_dump()))


def listar_duenos(db: Session) -> list[Dueno]:
    return listar(db, Dueno)


def obtener_dueno(db: Session, dueno_id: int) -> Dueno:
    return obtener_o_error(db, Dueno, dueno_id, ENTIDAD)


def actualizar_dueno(db: Session, dueno_id: int, datos: DuenoUpdate) -> Dueno:
    dueno = obtener_dueno(db, dueno_id)
    aplicar_cambios(dueno, datos.model_dump(exclude_unset=True))
    return guardar(db, dueno)


def eliminar_dueno(db: Session, dueno_id: int) -> None:
    dueno = obtener_dueno(db, dueno_id)
    eliminar(db, dueno, {
        "mascotas": "No se puede eliminar el dueño porque tiene "
                    "mascotas asociadas",
    })

"""Operaciones CRUD de la entidad Vacuna."""
from sqlalchemy.orm import Session

from src.crud.base import (
    aplicar_cambios,
    eliminar,
    guardar,
    listar,
    obtener_o_error,
    validar_referencia,
)
from src.database.models import Mascota, Vacuna
from src.schemas.vacuna import VacunaCreate, VacunaUpdate

ENTIDAD = "La vacuna"


def _validar_referencias(db: Session, cambios: dict) -> None:
    if "mascota_id" in cambios:
        validar_referencia(db, Mascota, cambios["mascota_id"], "La mascota")


def crear_vacuna(db: Session, datos: VacunaCreate) -> Vacuna:
    valores = datos.model_dump()
    _validar_referencias(db, valores)
    return guardar(db, Vacuna(**valores))


def listar_vacunas(db: Session) -> list[Vacuna]:
    return listar(db, Vacuna)


def obtener_vacuna(db: Session, vacuna_id: int) -> Vacuna:
    return obtener_o_error(db, Vacuna, vacuna_id, ENTIDAD)


def actualizar_vacuna(
    db: Session, vacuna_id: int, datos: VacunaUpdate
) -> Vacuna:
    vacuna = obtener_vacuna(db, vacuna_id)
    cambios = datos.model_dump(exclude_unset=True)
    _validar_referencias(db, cambios)
    aplicar_cambios(vacuna, cambios)
    return guardar(db, vacuna)


def eliminar_vacuna(db: Session, vacuna_id: int) -> None:
    eliminar(db, obtener_vacuna(db, vacuna_id), {})

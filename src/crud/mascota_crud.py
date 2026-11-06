"""Operaciones CRUD de la entidad Mascota."""
from sqlalchemy.orm import Session

from src.crud.base import (
    aplicar_cambios,
    eliminar,
    guardar,
    listar,
    obtener_o_error,
    validar_referencia,
)
from src.database.models import Dueno, Especie, Mascota
from src.schemas.mascota import MascotaCreate, MascotaUpdate

ENTIDAD = "La mascota"


def _validar_referencias(db: Session, cambios: dict) -> None:
    if "especie_id" in cambios:
        validar_referencia(db, Especie, cambios["especie_id"], "La especie")
    if "dueno_id" in cambios:
        validar_referencia(db, Dueno, cambios["dueno_id"], "El dueño")


def crear_mascota(db: Session, datos: MascotaCreate) -> Mascota:
    valores = datos.model_dump()
    _validar_referencias(db, valores)
    return guardar(db, Mascota(**valores))


def listar_mascotas(db: Session) -> list[Mascota]:
    return listar(db, Mascota)


def obtener_mascota(db: Session, mascota_id: int) -> Mascota:
    return obtener_o_error(db, Mascota, mascota_id, ENTIDAD)


def actualizar_mascota(
    db: Session, mascota_id: int, datos: MascotaUpdate
) -> Mascota:
    mascota = obtener_mascota(db, mascota_id)
    cambios = datos.model_dump(exclude_unset=True)
    _validar_referencias(db, cambios)
    aplicar_cambios(mascota, cambios)
    return guardar(db, mascota)


def eliminar_mascota(db: Session, mascota_id: int) -> None:
    mascota = obtener_mascota(db, mascota_id)
    eliminar(db, mascota, {
        "citas": "No se puede eliminar la mascota porque tiene citas "
                 "asociadas",
        "vacunas": "No se puede eliminar la mascota porque tiene vacunas "
                   "asociadas",
    })

"""Operaciones CRUD de la entidad Veterinario."""
from sqlalchemy.orm import Session

from src.crud.base import (
    aplicar_cambios,
    eliminar,
    guardar,
    listar,
    obtener_o_error,
)
from src.database.models import Veterinario
from src.schemas.veterinario import VeterinarioCreate, VeterinarioUpdate

ENTIDAD = "El veterinario"


def crear_veterinario(db: Session, datos: VeterinarioCreate) -> Veterinario:
    return guardar(db, Veterinario(**datos.model_dump()))


def listar_veterinarios(db: Session) -> list[Veterinario]:
    return listar(db, Veterinario)


def obtener_veterinario(db: Session, veterinario_id: int) -> Veterinario:
    return obtener_o_error(db, Veterinario, veterinario_id, ENTIDAD)


def actualizar_veterinario(
    db: Session, veterinario_id: int, datos: VeterinarioUpdate
) -> Veterinario:
    veterinario = obtener_veterinario(db, veterinario_id)
    aplicar_cambios(veterinario, datos.model_dump(exclude_unset=True))
    return guardar(db, veterinario)


def eliminar_veterinario(db: Session, veterinario_id: int) -> None:
    veterinario = obtener_veterinario(db, veterinario_id)
    eliminar(db, veterinario, {
        "citas": "No se puede eliminar el veterinario porque tiene citas "
                 "asociadas",
    })

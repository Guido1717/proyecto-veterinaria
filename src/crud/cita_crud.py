"""Operaciones CRUD de la entidad Cita."""
from sqlalchemy.orm import Session

from src.crud.base import (
    aplicar_cambios,
    eliminar,
    guardar,
    listar,
    obtener_o_error,
    validar_referencia,
)
from src.database.models import Cita, Mascota, Veterinario
from src.schemas.cita import CitaCreate, CitaUpdate

ENTIDAD = "La cita"


def _validar_referencias(db: Session, cambios: dict) -> None:
    if "mascota_id" in cambios:
        validar_referencia(db, Mascota, cambios["mascota_id"], "La mascota")
    if "veterinario_id" in cambios:
        validar_referencia(
            db, Veterinario, cambios["veterinario_id"], "El veterinario"
        )


def crear_cita(db: Session, datos: CitaCreate) -> Cita:
    valores = datos.model_dump()
    _validar_referencias(db, valores)
    return guardar(db, Cita(**valores))


def listar_citas(db: Session) -> list[Cita]:
    return listar(db, Cita)


def obtener_cita(db: Session, cita_id: int) -> Cita:
    return obtener_o_error(db, Cita, cita_id, ENTIDAD)


def actualizar_cita(db: Session, cita_id: int, datos: CitaUpdate) -> Cita:
    cita = obtener_cita(db, cita_id)
    cambios = datos.model_dump(exclude_unset=True)
    _validar_referencias(db, cambios)
    aplicar_cambios(cita, cambios)
    return guardar(db, cita)


def eliminar_cita(db: Session, cita_id: int) -> None:
    cita = obtener_cita(db, cita_id)
    eliminar(db, cita, {
        "consulta": "No se puede eliminar la cita porque tiene una consulta "
                    "registrada",
    })

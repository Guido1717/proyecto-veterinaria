"""Operaciones CRUD de la entidad Consulta.

Regla de negocio: una cita tiene como máximo una consulta. Al registrarla,
la cita pasa a estado "atendida".
"""
from sqlalchemy.orm import Session

from src.crud.base import (
    aplicar_cambios,
    eliminar,
    guardar,
    listar,
    obtener_o_error,
    validar_referencia,
)
from src.crud.excepciones import ConflictoIntegridad
from src.database.models import Cita, Consulta
from src.schemas.consulta import ConsultaCreate, ConsultaUpdate

ENTIDAD = "La consulta"
ESTADO_ATENDIDA = "atendida"


def crear_consulta(db: Session, datos: ConsultaCreate) -> Consulta:
    cita = validar_referencia(db, Cita, datos.cita_id, "La cita")
    if cita.consulta is not None:
        raise ConflictoIntegridad(
            f"La cita con id {cita.id} ya tiene una consulta registrada"
        )

    consulta = Consulta(**datos.model_dump())
    cita.estado = ESTADO_ATENDIDA
    return guardar(db, consulta)


def listar_consultas(db: Session) -> list[Consulta]:
    return listar(db, Consulta)


def obtener_consulta(db: Session, consulta_id: int) -> Consulta:
    return obtener_o_error(db, Consulta, consulta_id, ENTIDAD)


def actualizar_consulta(
    db: Session, consulta_id: int, datos: ConsultaUpdate
) -> Consulta:
    consulta = obtener_consulta(db, consulta_id)
    aplicar_cambios(consulta, datos.model_dump(exclude_unset=True))
    return guardar(db, consulta)


def eliminar_consulta(db: Session, consulta_id: int) -> None:
    consulta = obtener_consulta(db, consulta_id)
    eliminar(db, consulta, {
        "tratamientos": "No se puede eliminar la consulta porque tiene "
                        "tratamientos asociados",
    })

"""Funciones comunes que reutilizan los CRUD de todas las entidades."""
from typing import Any, TypeVar

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.crud.excepciones import (
    ConflictoIntegridad,
    ReferenciaInvalida,
    RegistroNoEncontrado,
)
from src.database.connection import Base

Modelo = TypeVar("Modelo", bound=Base)

MENSAJE_INTEGRIDAD = (
    "La operación no se pudo completar porque viola una restricción "
    "de la base de datos"
)


def listar(db: Session, modelo: type[Modelo]) -> list[Modelo]:
    """Devuelve todos los registros ordenados por id (o una lista vacía)."""
    return list(db.scalars(select(modelo).order_by(modelo.id)))


def obtener_o_error(
    db: Session, modelo: type[Modelo], registro_id: int, entidad: str
) -> Modelo:
    """Busca por id o lanza RegistroNoEncontrado (la API responde 404)."""
    registro = db.get(modelo, registro_id)
    if registro is None:
        raise RegistroNoEncontrado(f"{entidad} con id {registro_id} no existe")
    return registro


def validar_referencia(
    db: Session, modelo: type[Modelo], registro_id: int, entidad: str
) -> Modelo:
    """Verifica una llave foránea o lanza ReferenciaInvalida (400)."""
    registro = db.get(modelo, registro_id)
    if registro is None:
        raise ReferenciaInvalida(f"{entidad} con id {registro_id} no existe")
    return registro


def aplicar_cambios(registro: Modelo, cambios: dict[str, Any]) -> None:
    """Copia al registro solo los campos enviados en la petición."""
    for campo, valor in cambios.items():
        setattr(registro, campo, valor)


def guardar(db: Session, registro: Modelo) -> Modelo:
    """Confirma la transacción y devuelve el registro actualizado."""
    db.add(registro)
    _confirmar(db)
    db.refresh(registro)
    return registro


def eliminar(
    db: Session, registro: Modelo, dependencias: dict[str, str]
) -> None:
    """Elimina el registro si no tiene hijos asociados.

    dependencias relaciona el nombre de la relación con el mensaje que se
    muestra cuando esa relación tiene registros, por ejemplo
    {"mascotas": "No se puede eliminar el dueño porque tiene mascotas"}.
    """
    for relacion, mensaje in dependencias.items():
        if getattr(registro, relacion):
            raise ConflictoIntegridad(mensaje)
    db.delete(registro)
    _confirmar(db)


def _confirmar(db: Session) -> None:
    try:
        db.commit()
    except IntegrityError as error:
        db.rollback()
        raise ConflictoIntegridad(MENSAJE_INTEGRIDAD) from error

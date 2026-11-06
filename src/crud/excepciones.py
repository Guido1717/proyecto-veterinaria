"""Errores de negocio que lanzan las operaciones CRUD.

La capa de API los traduce a códigos HTTP (ver src/api/errores.py).
"""


class RegistroNoEncontrado(Exception):
    """El registro pedido por id no existe."""


class ReferenciaInvalida(Exception):
    """Una llave foránea apunta a un registro que no existe."""


class ConflictoIntegridad(Exception):
    """La operación rompe una regla de integridad (duplicado, hijos, etc.)."""

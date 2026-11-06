"""Crea las tablas y aplica los ajustes de esquema pendientes.

Uso: python -m src.database.migrate
"""
from sqlalchemy import inspect, text

from src.database import models  # noqa: F401  (registra los modelos)
from src.database.connection import Base, engine

RESTRICCION_CITA_UNICA = "uq_consultas_cita_id"


def asegurar_cita_unica_en_consultas():
    """Agrega UNIQUE(cita_id) a consultas si la tabla ya existía sin ella.

    create_all() no modifica tablas existentes, así que las bases creadas
    antes de este cambio necesitan este paso. Es idempotente.
    """
    inspector = inspect(engine)
    restricciones = inspector.get_unique_constraints("consultas")
    if any(r["column_names"] == ["cita_id"] for r in restricciones):
        print("La restricción UNIQUE de consultas.cita_id ya existe.")
        return

    with engine.begin() as conexion:
        conexion.execute(text(
            f"ALTER TABLE consultas ADD CONSTRAINT {RESTRICCION_CITA_UNICA} "
            "UNIQUE (cita_id)"
        ))
    print("Restricción UNIQUE agregada a consultas.cita_id.")


def migrar():
    print("Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    asegurar_cita_unica_en_consultas()
    print("¡Migración completada!")


if __name__ == "__main__":
    migrar()

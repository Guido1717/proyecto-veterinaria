from src.database.connection import SessionLocal
from src.database.models import Tratamiento, Consulta


def crear_tratamiento(consulta_id, medicamento, duracion_dias):
    session = SessionLocal()
    try:
        consulta = session.query(Consulta).filter(Consulta.id == consulta_id).first()
        if not consulta:
            print("Error: la consulta no existe")
            return None
        nuevo = Tratamiento(consulta_id=consulta_id, medicamento=medicamento, duracion_dias=duracion_dias)
        session.add(nuevo)
        session.commit()
        session.refresh(nuevo)
        return nuevo
    finally:
        session.close()


def listar_tratamientos():
    session = SessionLocal()
    try:
        return session.query(Tratamiento).all()
    finally:
        session.close()


def obtener_tratamiento(id):
    session = SessionLocal()
    try:
        return session.query(Tratamiento).filter(Tratamiento.id == id).first()
    finally:
        session.close()


def actualizar_tratamiento(id, medicamento=None, duracion_dias=None):
    session = SessionLocal()
    try:
        tratamiento = session.query(Tratamiento).filter(Tratamiento.id == id).first()
        if tratamiento:
            if medicamento:
                tratamiento.medicamento = medicamento
            if duracion_dias:
                tratamiento.duracion_dias = duracion_dias
            session.commit()
            session.refresh(tratamiento)
        return tratamiento
    finally:
        session.close()


def eliminar_tratamiento(id):
    session = SessionLocal()
    try:
        tratamiento = session.query(Tratamiento).filter(Tratamiento.id == id).first()
        if tratamiento:
            session.delete(tratamiento)
            session.commit()
            return True
        return False
    finally:
        session.close()
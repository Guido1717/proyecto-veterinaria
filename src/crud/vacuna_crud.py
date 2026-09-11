from src.database.connection import SessionLocal
from src.database.models import Vacuna, Mascota


def crear_vacuna(mascota_id, nombre, fecha_aplicacion):
    session = SessionLocal()
    try:
        mascota = session.query(Mascota).filter(Mascota.id == mascota_id).first()
        if not mascota:
            print("Error: la mascota no existe")
            return None
        nueva = Vacuna(mascota_id=mascota_id, nombre=nombre, fecha_aplicacion=fecha_aplicacion)
        session.add(nueva)
        session.commit()
        session.refresh(nueva)
        return nueva
    finally:
        session.close()


def listar_vacunas():
    session = SessionLocal()
    try:
        return session.query(Vacuna).all()
    finally:
        session.close()


def obtener_vacuna(id):
    session = SessionLocal()
    try:
        return session.query(Vacuna).filter(Vacuna.id == id).first()
    finally:
        session.close()


def actualizar_vacuna(id, nombre=None, fecha_aplicacion=None):
    session = SessionLocal()
    try:
        vacuna = session.query(Vacuna).filter(Vacuna.id == id).first()
        if vacuna:
            if nombre:
                vacuna.nombre = nombre
            if fecha_aplicacion:
                vacuna.fecha_aplicacion = fecha_aplicacion
            session.commit()
            session.refresh(vacuna)
        return vacuna
    finally:
        session.close()


def eliminar_vacuna(id):
    session = SessionLocal()
    try:
        vacuna = session.query(Vacuna).filter(Vacuna.id == id).first()
        if vacuna:
            session.delete(vacuna)
            session.commit()
            return True
        return False
    finally:
        session.close()
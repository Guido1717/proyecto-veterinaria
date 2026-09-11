from src.database.connection import SessionLocal
from src.database.models import Especie


def crear_especie(nombre, descripcion=""):
    session = SessionLocal()
    try:
        nueva = Especie(nombre=nombre, descripcion=descripcion)
        session.add(nueva)
        session.commit()
        session.refresh(nueva)
        return nueva
    finally:
        session.close()


def listar_especies():
    session = SessionLocal()
    try:
        return session.query(Especie).all()
    finally:
        session.close()


def obtener_especie(id):
    session = SessionLocal()
    try:
        return session.query(Especie).filter(Especie.id == id).first()
    finally:
        session.close()


def actualizar_especie(id, nombre=None, descripcion=None):
    session = SessionLocal()
    try:
        especie = session.query(Especie).filter(Especie.id == id).first()
        if especie:
            if nombre:
                especie.nombre = nombre
            if descripcion:
                especie.descripcion = descripcion
            session.commit()
            session.refresh(especie)
        return especie
    finally:
        session.close()


def eliminar_especie(id):
    session = SessionLocal()
    try:
        especie = session.query(Especie).filter(Especie.id == id).first()
        if especie:
            session.delete(especie)
            session.commit()
            return True
        return False
    finally:
        session.close()
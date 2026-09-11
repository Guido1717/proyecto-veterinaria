from src.database.connection import SessionLocal
from src.database.models import Dueno


def crear_dueno(nombre, telefono, direccion=""):
    session = SessionLocal()
    try:
        nuevo = Dueno(nombre=nombre, telefono=telefono, direccion=direccion)
        session.add(nuevo)
        session.commit()
        session.refresh(nuevo)
        return nuevo
    finally:
        session.close()


def listar_duenos():
    session = SessionLocal()
    try:
        return session.query(Dueno).all()
    finally:
        session.close()


def obtener_dueno(id):
    session = SessionLocal()
    try:
        return session.query(Dueno).filter(Dueno.id == id).first()
    finally:
        session.close()


def actualizar_dueno(id, nombre=None, telefono=None, direccion=None):
    session = SessionLocal()
    try:
        dueno = session.query(Dueno).filter(Dueno.id == id).first()
        if dueno:
            if nombre:
                dueno.nombre = nombre
            if telefono:
                dueno.telefono = telefono
            if direccion:
                dueno.direccion = direccion
            session.commit()
            session.refresh(dueno)
        return dueno
    finally:
        session.close()


def eliminar_dueno(id):
    session = SessionLocal()
    try:
        dueno = session.query(Dueno).filter(Dueno.id == id).first()
        if dueno:
            session.delete(dueno)
            session.commit()
            return True
        return False
    finally:
        session.close()
        session.close()
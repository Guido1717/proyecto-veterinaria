from src.database.connection import SessionLocal
from src.database.models import Veterinario


def crear_veterinario(nombre, especialidad, telefono):
    session = SessionLocal()
    try:
        nuevo = Veterinario(nombre=nombre, especialidad=especialidad, telefono=telefono)
        session.add(nuevo)
        session.commit()
        session.refresh(nuevo)
        return nuevo
    finally:
        session.close()


def listar_veterinarios():
    session = SessionLocal()
    try:
        return session.query(Veterinario).all()
    finally:
        session.close()


def obtener_veterinario(id):
    session = SessionLocal()
    try:
        return session.query(Veterinario).filter(Veterinario.id == id).first()
    finally:
        session.close()


def actualizar_veterinario(id, nombre=None, especialidad=None, telefono=None):
    session = SessionLocal()
    try:
        veterinario = session.query(Veterinario).filter(Veterinario.id == id).first()
        if veterinario:
            if nombre:
                veterinario.nombre = nombre
            if especialidad:
                veterinario.especialidad = especialidad
            if telefono:
                veterinario.telefono = telefono
            session.commit()
            session.refresh(veterinario)
        return veterinario
    finally:
        session.close()


def eliminar_veterinario(id):
    session = SessionLocal()
    try:
        veterinario = session.query(Veterinario).filter(Veterinario.id == id).first()
        if veterinario:
            session.delete(veterinario)
            session.commit()
            return True
        return False
    finally:
        session.close()
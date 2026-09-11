from src.database.connection import SessionLocal
from src.database.models import Mascota


def crear_mascota(nombre, edad, especie_id, dueno_id):
    session = SessionLocal()
    try:
        # Validamos que existan la especie y el dueño usando el mismo session
        # (más eficiente que abrir sesiones nuevas con obtener_especie/obtener_dueno)
        from src.database.models import Especie, Dueno

        especie = session.query(Especie).filter(Especie.id == especie_id).first()
        if not especie:
            print("Error: la especie no existe")
            return None

        dueno = session.query(Dueno).filter(Dueno.id == dueno_id).first()
        if not dueno:
            print("Error: el dueño no existe")
            return None

        nueva = Mascota(nombre=nombre, edad=edad, especie_id=especie_id, dueno_id=dueno_id)
        session.add(nueva)
        session.commit()
        session.refresh(nueva)
        return nueva
    finally:
        session.close()


def listar_mascotas():
    session = SessionLocal()
    try:
        return session.query(Mascota).all()
    finally:
        session.close()


def obtener_mascota(id):
    session = SessionLocal()
    try:
        return session.query(Mascota).filter(Mascota.id == id).first()
    finally:
        session.close()


def actualizar_mascota(id, nombre=None, edad=None):
    session = SessionLocal()
    try:
        mascota = session.query(Mascota).filter(Mascota.id == id).first()
        if mascota:
            if nombre:
                mascota.nombre = nombre
            if edad:
                mascota.edad = edad
            session.commit()
            session.refresh(mascota)
        return mascota
    finally:
        session.close()


def eliminar_mascota(id):
    session = SessionLocal()
    try:
        mascota = session.query(Mascota).filter(Mascota.id == id).first()
        if mascota:
            session.delete(mascota)
            session.commit()
            return True
        return False
    finally:
        session.close()
from datetime import date, datetime
from src.database.connection import SessionLocal
from src.database.models import Cita, Mascota, Veterinario


def _parsear_fecha(fecha):
    """Permite pasar la fecha como 'YYYY-MM-DD' (texto) o como objeto date."""
    if isinstance(fecha, str):
        return datetime.strptime(fecha, "%Y-%m-%d").date()
    return fecha


def crear_cita(fecha, mascota_id, veterinario_id):
    session = SessionLocal()
    try:
        mascota = session.query(Mascota).filter(Mascota.id == mascota_id).first()
        if not mascota:
            print("Error: la mascota no existe")
            return None

        veterinario = session.query(Veterinario).filter(Veterinario.id == veterinario_id).first()
        if not veterinario:
            print("Error: el veterinario no existe")
            return None

        nueva = Cita(
            fecha=_parsear_fecha(fecha),
            mascota_id=mascota_id,
            veterinario_id=veterinario_id,
        )
        session.add(nueva)
        session.commit()
        session.refresh(nueva)
        return nueva
    finally:
        session.close()


def listar_citas():
    session = SessionLocal()
    try:
        return session.query(Cita).all()
    finally:
        session.close()


def obtener_cita(id):
    session = SessionLocal()
    try:
        return session.query(Cita).filter(Cita.id == id).first()
    finally:
        session.close()


def actualizar_cita(id, fecha=None, estado=None):
    session = SessionLocal()
    try:
        cita = session.query(Cita).filter(Cita.id == id).first()
        if cita:
            if fecha:
                cita.fecha = _parsear_fecha(fecha)
            if estado:
                cita.estado = estado
            session.commit()
            session.refresh(cita)
        return cita
    finally:
        session.close()


def eliminar_cita(id):
    session = SessionLocal()
    try:
        cita = session.query(Cita).filter(Cita.id == id).first()
        if cita:
            session.delete(cita)
            session.commit()
            return True
        return False
    finally:
        session.close()
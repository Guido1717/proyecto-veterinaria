from src.database.connection import SessionLocal
from src.database.models import Consulta, Cita


def crear_consulta(cita_id, diagnostico, observaciones=""):
    session = SessionLocal()
    try:
        cita = session.query(Cita).filter(Cita.id == cita_id).first()
        if not cita:
            print("Error: la cita no existe")
            return None

        if cita.consulta:
            print("Error: esta cita ya tiene una consulta registrada")
            return None

        nueva = Consulta(
            cita_id=cita_id,
            diagnostico=diagnostico,
            observaciones=observaciones,
        )
        session.add(nueva)

        cita.estado = "atendida"

        session.commit()
        session.refresh(nueva)
        return nueva
    finally:
        session.close()


def listar_consultas():
    session = SessionLocal()
    try:
        return session.query(Consulta).all()
    finally:
        session.close()


def obtener_consulta(id):
    session = SessionLocal()
    try:
        return session.query(Consulta).filter(Consulta.id == id).first()
    finally:
        session.close()


def actualizar_consulta(id, diagnostico=None, observaciones=None):
    session = SessionLocal()
    try:
        consulta = session.query(Consulta).filter(Consulta.id == id).first()
        if consulta:
            if diagnostico:
                consulta.diagnostico = diagnostico
            if observaciones:
                consulta.observaciones = observaciones
            session.commit()
            session.refresh(consulta)
        return consulta
    finally:
        session.close()


def eliminar_consulta(id):
    session = SessionLocal()
    try:
        consulta = session.query(Consulta).filter(Consulta.id == id).first()
        if consulta:
            session.delete(consulta)
            session.commit()
            return True
        return False
    finally:
        session.close()
from src.entities.consulta import Consulta
from src.crud.cita_crud import obtener_cita, actualizar_cita

consultas = []
siguiente_id = 1

def crear_consulta(cita_id, diagnostico, observaciones=""):
    global siguiente_id
    cita = obtener_cita(cita_id)
    if not cita:
        print("Error: la cita no existe")
        return None
    nueva = Consulta(siguiente_id, cita_id, diagnostico, observaciones)
    consultas.append(nueva)
    siguiente_id += 1
    actualizar_cita(cita_id, estado="atendida")
    return nueva

def listar_consultas():
    return consultas

def obtener_consulta(id):
    for c in consultas:
        if c.id == id:
            return c
    return None

def actualizar_consulta(id, diagnostico=None, observaciones=None):
    consulta = obtener_consulta(id)
    if consulta:
        if diagnostico:
            consulta.diagnostico = diagnostico
        if observaciones:
            consulta.observaciones = observaciones
    return consulta

def eliminar_consulta(id):
    consulta = obtener_consulta(id)
    if consulta:
        consultas.remove(consulta)
        return True
    return False
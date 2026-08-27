from src.entities.tratamiento import Tratamiento
from src.crud.consulta_crud import obtener_consulta

tratamientos = []
siguiente_id = 1

def crear_tratamiento(consulta_id, medicamento, duracion_dias):
    global siguiente_id
    if not obtener_consulta(consulta_id):
        print("Error: la consulta no existe")
        return None
    nuevo = Tratamiento(siguiente_id, consulta_id, medicamento, duracion_dias)
    tratamientos.append(nuevo)
    siguiente_id += 1
    return nuevo

def listar_tratamientos():
    return tratamientos

def obtener_tratamiento(id):
    for t in tratamientos:
        if t.id == id:
            return t
    return None

def actualizar_tratamiento(id, medicamento=None, duracion_dias=None):
    tratamiento = obtener_tratamiento(id)
    if tratamiento:
        if medicamento:
            tratamiento.medicamento = medicamento
        if duracion_dias:
            tratamiento.duracion_dias = duracion_dias
    return tratamiento

def eliminar_tratamiento(id):
    tratamiento = obtener_tratamiento(id)
    if tratamiento:
        tratamientos.remove(tratamiento)
        return True
    return False
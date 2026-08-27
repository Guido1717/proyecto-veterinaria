from src.entities.cita import Cita
from src.crud.mascota_crud import obtener_mascota
from src.crud.veterinario_crud import obtener_veterinario

citas = []
siguiente_id = 1

def crear_cita(fecha, mascota_id, veterinario_id):
    global siguiente_id
    if not obtener_mascota(mascota_id):
        print("Error: la mascota no existe")
        return None
    if not obtener_veterinario(veterinario_id):
        print("Error: el veterinario no existe")
        return None
    nueva = Cita(siguiente_id, fecha, mascota_id, veterinario_id)
    citas.append(nueva)
    siguiente_id += 1
    return nueva

def listar_citas():
    return citas

def obtener_cita(id):
    for c in citas:
        if c.id == id:
            return c
    return None

def actualizar_cita(id, fecha=None, estado=None):
    cita = obtener_cita(id)
    if cita:
        if fecha:
            cita.fecha = fecha
        if estado:
            cita.estado = estado
    return cita

def eliminar_cita(id):
    cita = obtener_cita(id)
    if cita:
        citas.remove(cita)
        return True
    return False
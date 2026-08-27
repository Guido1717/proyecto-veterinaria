from src.entities.vacuna import Vacuna
from src.crud.mascota_crud import obtener_mascota

vacunas = []
siguiente_id = 1

def crear_vacuna(mascota_id, nombre, fecha_aplicacion):
    global siguiente_id
    if not obtener_mascota(mascota_id):
        print("Error: la mascota no existe")
        return None
    nueva = Vacuna(siguiente_id, mascota_id, nombre, fecha_aplicacion)
    vacunas.append(nueva)
    siguiente_id += 1
    return nueva

def listar_vacunas():
    return vacunas

def obtener_vacuna(id):
    for v in vacunas:
        if v.id == id:
            return v
    return None

def actualizar_vacuna(id, nombre=None, fecha_aplicacion=None):
    vacuna = obtener_vacuna(id)
    if vacuna:
        if nombre:
            vacuna.nombre = nombre
        if fecha_aplicacion:
            vacuna.fecha_aplicacion = fecha_aplicacion
    return vacuna

def eliminar_vacuna(id):
    vacuna = obtener_vacuna(id)
    if vacuna:
        vacunas.remove(vacuna)
        return True
    return False
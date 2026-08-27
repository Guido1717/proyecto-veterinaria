from src.entities.mascota import Mascota
from src.crud.especie_crud import obtener_especie
from src.crud.dueno_crud import obtener_dueno

mascotas = []
siguiente_id = 1

def crear_mascota(nombre, edad, especie_id, dueno_id):
    global siguiente_id
    if not obtener_especie(especie_id):
        print("Error: la especie no existe")
        return None
    if not obtener_dueno(dueno_id):
        print("Error: el dueño no existe")
        return None
    nueva = Mascota(siguiente_id, nombre, edad, especie_id, dueno_id)
    mascotas.append(nueva)
    siguiente_id += 1
    return nueva

def listar_mascotas():
    return mascotas

def obtener_mascota(id):
    for m in mascotas:
        if m.id == id:
            return m
    return None

def actualizar_mascota(id, nombre=None, edad=None):
    mascota = obtener_mascota(id)
    if mascota:
        if nombre:
            mascota.nombre = nombre
        if edad:
            mascota.edad = edad
    return mascota

def eliminar_mascota(id):
    mascota = obtener_mascota(id)
    if mascota:
        mascotas.remove(mascota)
        return True
    return False
from src.entities.dueno import Dueno

duenos = []
siguiente_id = 1

def crear_dueno(nombre, telefono, direccion=""):
    global siguiente_id
    nuevo = Dueno(siguiente_id, nombre, telefono, direccion)
    duenos.append(nuevo)
    siguiente_id += 1
    return nuevo

def listar_duenos():
    return duenos

def obtener_dueno(id):
    for d in duenos:
        if d.id == id:
            return d
    return None

def actualizar_dueno(id, nombre=None, telefono=None, direccion=None):
    dueno = obtener_dueno(id)
    if dueno:
        if nombre:
            dueno.nombre = nombre
        if telefono:
            dueno.telefono = telefono
        if direccion:
            dueno.direccion = direccion
    return dueno

def eliminar_dueno(id):
    dueno = obtener_dueno(id)
    if dueno:
        duenos.remove(dueno)
        return True
    return False
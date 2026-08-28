from src.entities.especie import Especie

# Lista en memoria que almacena las especies registradas
especies = []
siguiente_id = 1

def crear_especie(nombre, descripcion=""):
    global siguiente_id
    nueva = Especie(siguiente_id, nombre, descripcion)
    especies.append(nueva)
    siguiente_id += 1
    return nueva

def listar_especies():
    return especies

def obtener_especie(id):
    for e in especies:
        if e.id == id:
            return e
    return None

def actualizar_especie(id, nombre=None, descripcion=None):
    especie = obtener_especie(id)
    if especie:
        if nombre:
            especie.nombre = nombre
        if descripcion:
            especie.descripcion = descripcion
    return especie

def eliminar_especie(id):
    especie = obtener_especie(id)
    if especie:
        especies.remove(especie)
        return True
    return False
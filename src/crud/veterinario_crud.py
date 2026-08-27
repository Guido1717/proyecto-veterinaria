from src.entities.veterinario import Veterinario

veterinarios = []
siguiente_id = 1

def crear_veterinario(nombre, especialidad, telefono):
    global siguiente_id
    nuevo = Veterinario(siguiente_id, nombre, especialidad, telefono)
    veterinarios.append(nuevo)
    siguiente_id += 1
    return nuevo

def listar_veterinarios():
    return veterinarios

def obtener_veterinario(id):
    for v in veterinarios:
        if v.id == id:
            return v
    return None

def actualizar_veterinario(id, nombre=None, especialidad=None, telefono=None):
    veterinario = obtener_veterinario(id)
    if veterinario:
        if nombre:
            veterinario.nombre = nombre
        if especialidad:
            veterinario.especialidad = especialidad
        if telefono:
            veterinario.telefono = telefono
    return veterinario

def eliminar_veterinario(id):
    veterinario = obtener_veterinario(id)
    if veterinario:
        veterinarios.remove(veterinario)
        return True
    return False
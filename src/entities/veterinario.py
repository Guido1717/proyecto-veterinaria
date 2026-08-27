class Veterinario:
    def __init__(self, id, nombre, especialidad, telefono):
        self.id = id
        self.nombre = nombre
        self.especialidad = especialidad
        self.telefono = telefono

    def __str__(self):
        return f"[{self.id}] Dr(a). {self.nombre} - {self.especialidad}"
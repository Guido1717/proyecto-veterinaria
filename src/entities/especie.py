class Especie:
    def __init__(self, id, nombre, descripcion=""):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"[{self.id}] {self.nombre} - {self.descripcion}"
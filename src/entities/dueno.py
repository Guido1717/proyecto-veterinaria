class Dueno:
    def __init__(self, id, nombre, telefono, direccion=""):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return f"[{self.id}] {self.nombre} - Tel: {self.telefono}"
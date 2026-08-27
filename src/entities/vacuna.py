class Vacuna:
    def __init__(self, id, mascota_id, nombre, fecha_aplicacion):
        self.id = id
        self.mascota_id = mascota_id
        self.nombre = nombre
        self.fecha_aplicacion = fecha_aplicacion

    def __str__(self):
        return f"[{self.id}] {self.nombre} - Aplicada: {self.fecha_aplicacion}"
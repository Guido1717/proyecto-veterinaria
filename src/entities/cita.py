class Cita:
    def __init__(self, id, fecha, mascota_id, veterinario_id, estado="pendiente"):
        self.id = id
        self.fecha = fecha
        self.mascota_id = mascota_id
        self.veterinario_id = veterinario_id
        self.estado = estado

    def __str__(self):
        return f"[{self.id}] Cita {self.fecha} - Estado: {self.estado}"
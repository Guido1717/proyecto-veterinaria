class Tratamiento:
    def __init__(self, id, consulta_id, medicamento, duracion_dias):
        self.id = id
        self.consulta_id = consulta_id
        self.medicamento = medicamento
        self.duracion_dias = duracion_dias

    def __str__(self):
        return f"[{self.id}] {self.medicamento} - {self.duracion_dias} días"
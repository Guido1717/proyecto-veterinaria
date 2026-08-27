class Consulta:
    def __init__(self, id, cita_id, diagnostico, observaciones=""):
        self.id = id
        self.cita_id = cita_id
        self.diagnostico = diagnostico
        self.observaciones = observaciones

    def __str__(self):
        return f"[{self.id}] Consulta - {self.diagnostico}"
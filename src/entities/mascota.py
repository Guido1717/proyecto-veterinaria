class Mascota:
    def __init__(self, id, nombre, edad, especie_id, dueno_id):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.especie_id = especie_id
        self.dueno_id = dueno_id

    def __str__(self):
        return f"[{self.id}] {self.nombre} - {self.edad} años"
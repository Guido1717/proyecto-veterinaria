from src.crud.especie_crud import crear_especie, listar_especies
from src.crud.dueno_crud import crear_dueno, listar_duenos
from src.crud.mascota_crud import crear_mascota, listar_mascotas, actualizar_mascota
from src.crud.veterinario_crud import crear_veterinario, listar_veterinarios
from src.crud.cita_crud import crear_cita, listar_citas
from src.crud.consulta_crud import crear_consulta, listar_consultas
from src.crud.vacuna_crud import crear_vacuna, listar_vacunas, eliminar_vacuna
from src.crud.tratamiento_crud import crear_tratamiento, listar_tratamientos, actualizar_tratamiento

print("=== SISTEMA VETERINARIA ===\n")

e1 = crear_especie("Canino", "Perros de cualquier raza")
e2 = crear_especie("Felino", "Gatos de cualquier raza")

d1 = crear_dueno("Carlos Pérez", "3001234567", "Calle 10 #5-20")
d2 = crear_dueno("Ana Gómez", "3109876543", "Carrera 15 #8-30")

m1 = crear_mascota("Rocky", 3, e1.id, d1.id)
m2 = crear_mascota("Michi", 2, e2.id, d2.id)

v1 = crear_veterinario("Laura Torres", "Medicina general", "3201112233")
v2 = crear_veterinario("Andrés Ruiz", "Cirugía", "3159998877")

c1 = crear_cita("2026-08-30", m1.id, v1.id)
c2 = crear_cita("2026-09-02", m2.id, v2.id)

print("--- Citas antes de la consulta ---")
for c in listar_citas():
    print(c)

con1 = crear_consulta(c1.id, "Chequeo general, todo normal", "Peso adecuado")
con2 = crear_consulta(c2.id, "Vómito leve", "Se recomienda dieta blanda")

print("\n--- Citas después de la consulta (estado actualizado) ---")
for c in listar_citas():
    print(c)

vac1 = crear_vacuna(m1.id, "Rabia", "2026-08-15")

t1 = crear_tratamiento(con2.id, "Antiemético", 5)

print("\n--- Datos actuales ---")
print("Especies:", [str(e) for e in listar_especies()])
print("Dueños:", [str(d) for d in listar_duenos()])
print("Mascotas:", [str(m) for m in listar_mascotas()])
print("Veterinarios:", [str(v) for v in listar_veterinarios()])
print("Vacunas:", [str(v) for v in listar_vacunas()])
print("Tratamientos:", [str(t) for t in listar_tratamientos()])

actualizar_mascota(m1.id, edad=4)
actualizar_tratamiento(t1.id, duracion_dias=7)
print("\n--- Después de actualizar edad de Rocky y duración del tratamiento ---")
print(listar_mascotas()[0])
print(listar_tratamientos()[0])

eliminar_vacuna(vac1.id)
print("\n--- Después de eliminar la vacuna ---")
print("Vacunas restantes:", listar_vacunas())

print("\n--- Relación completa: Cita -> Mascota -> Dueño/Especie -> Veterinario ---")
for cita in listar_citas():
    mascota = next(m for m in listar_mascotas() if m.id == cita.mascota_id)
    dueno = next(d for d in listar_duenos() if d.id == mascota.dueno_id)
    especie = next(e for e in listar_especies() if e.id == mascota.especie_id)
    veterinario = next(v for v in listar_veterinarios() if v.id == cita.veterinario_id)
    print(f"{cita} | Mascota: {mascota.nombre} ({especie.nombre}) | Dueño: {dueno.nombre} | Vet: {veterinario.nombre}")
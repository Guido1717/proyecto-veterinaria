from src.crud.especie_crud import crear_especie, listar_especies
from src.crud.dueno_crud import crear_dueno, listar_duenos
from src.crud.mascota_crud import crear_mascota, listar_mascotas, actualizar_mascota
from src.crud.veterinario_crud import crear_veterinario, listar_veterinarios
from src.crud.cita_crud import crear_cita, listar_citas
from src.crud.consulta_crud import crear_consulta, listar_consultas
from src.crud.vacuna_crud import crear_vacuna, listar_vacunas, eliminar_vacuna
from src.crud.tratamiento_crud import crear_tratamiento, listar_tratamientos, actualizar_tratamiento
from datetime import date

print("=== SISTEMA VETERINARIA (conectado a Neon PostgreSQL) ===\n")

# Sección de registro: gestiona especies, dueños, mascotas y veterinarios
# --- Crear especies ---
e1 = crear_especie("Bovino", "Ganado vacuno")
e2 = crear_especie("Equino", "Caballos")

# --- Crear dueños ---
d1 = crear_dueno("Marta Ríos", "3021239876", "Vereda La Esperanza")
d2 = crear_dueno("Jorge Salas", "3187654321", "Finca El Roble")

# --- Crear mascotas ---
m1 = crear_mascota("Toro", 5, e1.id, d1.id)
m2 = crear_mascota("Estrella", 4, e2.id, d2.id)

# --- Crear veterinarios ---
v1 = crear_veterinario("Camila Ortiz", "Medicina veterinaria general", "3211112233")
v2 = crear_veterinario("Felipe Nieto", "Zootecnia", "3229998877")

# Sección de atención clínica: gestiona citas, consultas, vacunas y tratamientos
# --- Crear citas ---
c1 = crear_cita(date(2026, 9, 15), m1.id, v1.id)
c2 = crear_cita(date(2026, 9, 18), m2.id, v2.id)

print("--- Citas antes de la consulta ---")
for c in listar_citas():
    print(c.id, c.fecha, c.estado)

# --- Crear consultas (actualiza el estado de la cita automáticamente) ---
con1 = crear_consulta(c1.id, "Chequeo general, todo normal", "Buen estado nutricional")
con2 = crear_consulta(c2.id, "Cojera leve en pata trasera", "Se recomienda reposo")

print("\n--- Citas después de la consulta (estado actualizado) ---")
for c in listar_citas():
    print(c.id, c.fecha, c.estado)

# --- Crear vacunas ---
vac1 = crear_vacuna(m1.id, "Fiebre aftosa", date(2026, 9, 1))

# --- Crear tratamientos ---
t1 = crear_tratamiento(con2.id, "Antiinflamatorio", 7)

print("\n--- Datos actuales ---")
print("Especies:", [(e.id, e.nombre) for e in listar_especies()])
print("Dueños:", [(d.id, d.nombre) for d in listar_duenos()])
print("Mascotas:", [(m.id, m.nombre) for m in listar_mascotas()])
print("Veterinarios:", [(v.id, v.nombre) for v in listar_veterinarios()])
print("Vacunas:", [(v.id, v.nombre) for v in listar_vacunas()])
print("Tratamientos:", [(t.id, t.medicamento) for t in listar_tratamientos()])

# --- Actualizar (UPDATE) ---
actualizar_mascota(m1.id, edad=6)
actualizar_tratamiento(t1.id, duracion_dias=10)
print("\n--- Después de actualizar edad de Toro y duración del tratamiento ---")
print("Edad actualizada:", [(m.id, m.nombre, m.edad) for m in listar_mascotas() if m.id == m1.id])
print("Tratamiento actualizado:", [(t.id, t.medicamento, t.duracion_dias) for t in listar_tratamientos() if t.id == t1.id])

# --- Eliminar (DELETE) ---
eliminar_vacuna(vac1.id)
print("\n--- Después de eliminar la vacuna ---")
print("Vacunas restantes:", [(v.id, v.nombre) for v in listar_vacunas()])

# --- Mostrar relaciones completas ---
print("\n--- Relación completa: Cita -> Mascota -> Dueño/Especie -> Veterinario ---")
for cita in listar_citas():
    mascota = next(m for m in listar_mascotas() if m.id == cita.mascota_id)
    dueno = next(d for d in listar_duenos() if d.id == mascota.dueno_id)
    especie = next(e for e in listar_especies() if e.id == mascota.especie_id)
    veterinario = next(v for v in listar_veterinarios() if v.id == cita.veterinario_id)
    print(f"Cita {cita.id} ({cita.fecha}, {cita.estado}) | Mascota: {mascota.nombre} ({especie.nombre}) | Dueño: {dueno.nombre} | Vet: {veterinario.nombre}")

print("\n=== Verifica los cambios directamente en el panel de Neon ===")
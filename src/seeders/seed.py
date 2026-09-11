from src.database.connection import SessionLocal
from src.database.models import (
    Especie, Dueno, Mascota, Veterinario, Cita, Consulta, Vacuna, Tratamiento
)
from datetime import date


def seed():
    session = SessionLocal()

    try:
        # --- Especies ---
        e1 = Especie(nombre="Canino", descripcion="Perros de cualquier raza")
        e2 = Especie(nombre="Felino", descripcion="Gatos de cualquier raza")
        session.add_all([e1, e2])
        session.commit()

        # --- Dueños ---
        d1 = Dueno(nombre="Carlos Pérez", telefono="3001234567", direccion="Calle 10 #5-20")
        d2 = Dueno(nombre="Ana Gómez", telefono="3109876543", direccion="Carrera 15 #8-30")
        session.add_all([d1, d2])
        session.commit()

        # --- Mascotas (dependen de especie y dueño) ---
        m1 = Mascota(nombre="Rocky", edad=3, especie_id=e1.id, dueno_id=d1.id)
        m2 = Mascota(nombre="Michi", edad=2, especie_id=e2.id, dueno_id=d2.id)
        session.add_all([m1, m2])
        session.commit()

        # --- Veterinarios ---
        v1 = Veterinario(nombre="Laura Torres", especialidad="Medicina general", telefono="3201112233")
        v2 = Veterinario(nombre="Andrés Ruiz", especialidad="Cirugía", telefono="3159998877")
        session.add_all([v1, v2])
        session.commit()

        # --- Citas (dependen de mascota y veterinario) ---
        c1 = Cita(fecha=date(2026, 9, 5), mascota_id=m1.id, veterinario_id=v1.id, estado="pendiente")
        c2 = Cita(fecha=date(2026, 9, 8), mascota_id=m2.id, veterinario_id=v2.id, estado="pendiente")
        session.add_all([c1, c2])
        session.commit()

        # --- Consultas (dependen de cita) ---
        con1 = Consulta(diagnostico="Chequeo general, todo normal", observaciones="Peso adecuado", cita_id=c1.id)
        session.add(con1)
        session.commit()

        # --- Vacunas (dependen de mascota) ---
        vac1 = Vacuna(nombre="Rabia", fecha_aplicacion=date(2026, 8, 15), mascota_id=m1.id)
        session.add(vac1)
        session.commit()

        # --- Tratamientos (dependen de consulta) ---
        t1 = Tratamiento(medicamento="Antiemético", duracion_dias=5, consulta_id=con1.id)
        session.add(t1)
        session.commit()

        print("¡Seeders ejecutados exitosamente! Datos de prueba insertados en las 8 tablas.")

    except Exception as e:
        session.rollback()
        print(f"Error al ejecutar los seeders: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    seed()
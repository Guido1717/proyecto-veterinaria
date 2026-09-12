# Proyecto Veterinaria

Sistema de gestión para una clínica veterinaria, desarrollado como proyecto para el segundo examen de Programación de Software. Permite administrar dueños, mascotas, veterinarios, citas, consultas, vacunas y tratamientos.

## Tecnologías

- Python
- SQLAlchemy (ORM)
- PostgreSQL (Neon)

## Entidades

- Dueño
- Mascota
- Especie
- Veterinario
- Cita
- Consulta
- Vacuna
- Tratamiento

Cada entidad cuenta con su propio módulo CRUD (crear, listar, obtener, actualizar, eliminar) ubicado en `src/crud/`.

## Instalación

\`\`\`bash
git clone https://github.com/Guido1717/proyecto-veterinaria.git
cd proyecto-veterinaria
pip install -r requirements.txt
\`\`\`

Configura la variable de entorno con la cadena de conexión a tu base de datos Neon (por ejemplo en un archivo `.env`):

\`\`\`
DATABASE_URL=postgresql://usuario:contraseña@host/nombre_bd
\`\`\`

## Ejecución

\`\`\`bash
python main.py
\`\`\`

## Video de sustentación

[Ver video](https://drive.google.com/file/d/1tR69Oj9tb5zgE70kZCg3JJvpaYAI7arc/view?usp=drivesdk)

## Autor

Guido1717

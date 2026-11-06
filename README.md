# Proyecto Veterinaria – API REST

API REST con **FastAPI** para gestionar una veterinaria: especies, dueños,
mascotas, veterinarios, citas, consultas, vacunas y tratamientos. Usa
**SQLAlchemy** sobre **PostgreSQL (Neon)**.

## Requisitos

- Python 3.12 o superior
- Una base de datos PostgreSQL (por ejemplo, un proyecto en Neon)

## Instalación

```bash
python -m venv .venv
```

Activa el entorno virtual:

- Windows (PowerShell): `.\.venv\Scripts\Activate.ps1`
- Linux / macOS: `source .venv/bin/activate`

Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Configuración

Copia `.env.example` como `.env` y escribe tu cadena de conexión real:

```env
DATABASE_URL=postgresql://USUARIO:CONTRASENA@HOST/BASE_DE_DATOS?sslmode=require
```

El archivo `.env` está en `.gitignore`: **no lo subas al repositorio**.

Opcionalmente, `CORS_ORIGINS` define qué orígenes del frontend pueden llamar
a la API (por defecto `http://localhost:4200,http://127.0.0.1:4200`).

## Base de datos

Crear las tablas (y la restricción UNIQUE de `consultas.cita_id`):

```bash
python -m src.database.migrate
```

Insertar datos de prueba (opcional):

```bash
python -m src.seeders.seed
```

## Levantar la API

```bash
uvicorn main:app --reload --port 8000
```

- API: <http://localhost:8000>
- Swagger: <http://localhost:8000/docs>
- ReDoc: <http://localhost:8000/redoc>

## Endpoints

Cada entidad tiene 5 endpoints. Las rutas de colección terminan en `/`.

| Método | Ruta | Acción | Éxito |
|---|---|---|---|
| GET | `/<recurso>/` | Listar (lista vacía si no hay registros) | 200 |
| GET | `/<recurso>/{id}` | Obtener por id | 200 |
| POST | `/<recurso>/` | Crear | 201 |
| PUT | `/<recurso>/{id}` | Actualizar solo los campos enviados | 200 |
| DELETE | `/<recurso>/{id}` | Eliminar | 204 |

Recursos: `especies`, `duenos`, `mascotas`, `veterinarios`, `citas`,
`consultas`, `vacunas`, `tratamientos`.

Errores (cuerpo `{"detail": "..."}`):

| Código | Cuándo |
|---|---|
| 400 | Una llave foránea apunta a un registro que no existe |
| 404 | El registro pedido no existe |
| 409 | Cita con consulta duplicada, o eliminar un registro con hijos asociados |
| 422 | Datos inválidos (tipos, longitudes, campos requeridos, `null` en PUT) |

Reglas de negocio:

- Una cita tiene como máximo una consulta. Al registrarla, la cita pasa a
  estado `atendida`.
- El estado de una cita es `pendiente`, `atendida` o `cancelada`.
- Las fechas usan el formato ISO `YYYY-MM-DD`.

## Estructura

```text
main.py                  App FastAPI: CORS y registro de routers
src/api/routers/         Un APIRouter por entidad
src/api/dependencias.py  Sesión de base de datos por petición
src/api/errores.py       Errores de negocio -> códigos HTTP
src/schemas/             Schemas Pydantic Create / Update / Read
src/crud/                Operaciones CRUD con SQLAlchemy
src/database/            Conexión, modelos y migración
src/seeders/seed.py      Datos de prueba
scripts/probar_endpoints.py  Prueba de los 40 endpoints
```

## Probar los endpoints

Con la API levantada, en otra terminal:

```bash
python scripts/probar_endpoints.py
```

El script crea sus propios registros, prueba los 40 endpoints y los casos de
error, y al final borra lo que creó.

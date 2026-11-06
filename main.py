"""API REST de la veterinaria (FastAPI).

Levantar en local:  uvicorn main:app --reload --port 8000
Documentación:      http://localhost:8000/docs
"""
import os

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from src.api.errores import registrar_manejadores
from src.api.routers import (
    citas,
    consultas,
    duenos,
    especies,
    mascotas,
    tratamientos,
    vacunas,
    veterinarios,
)

# Orígenes del frontend que pueden llamar a la API. Se pueden cambiar con la
# variable CORS_ORIGINS (lista separada por comas) en el archivo .env.
ORIGENES_POR_DEFECTO = "http://localhost:4200,http://127.0.0.1:4200"
ORIGENES_PERMITIDOS = [
    origen.strip()
    for origen in os.getenv("CORS_ORIGINS", ORIGENES_POR_DEFECTO).split(",")
    if origen.strip()
]

ROUTERS = (
    especies.router,
    duenos.router,
    mascotas.router,
    veterinarios.router,
    citas.router,
    consultas.router,
    vacunas.router,
    tratamientos.router,
)

app = FastAPI(
    title="API Veterinaria",
    description="CRUD de especies, dueños, mascotas, veterinarios, citas, "
                "consultas, vacunas y tratamientos.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGENES_PERMITIDOS,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

registrar_manejadores(app)

for router in ROUTERS:
    app.include_router(router)


@app.get("/", status_code=status.HTTP_200_OK, tags=["Estado"])
def estado():
    """Comprueba que la API está en línea."""
    return {"estado": "ok", "documentacion": "/docs"}

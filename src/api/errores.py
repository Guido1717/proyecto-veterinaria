"""Traducción de los errores del CRUD a respuestas HTTP."""
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from src.crud.excepciones import (
    ConflictoIntegridad,
    ReferenciaInvalida,
    RegistroNoEncontrado,
)

CODIGO_POR_EXCEPCION = {
    RegistroNoEncontrado: status.HTTP_404_NOT_FOUND,
    ReferenciaInvalida: status.HTTP_400_BAD_REQUEST,
    ConflictoIntegridad: status.HTTP_409_CONFLICT,
}


class MensajeError(BaseModel):
    detail: str


# Documentación de las respuestas de error para Swagger (/docs).
RESPUESTA_400 = {
    status.HTTP_400_BAD_REQUEST: {
        "model": MensajeError,
        "description": "Una llave foránea apunta a un registro inexistente",
    },
}
RESPUESTA_404 = {
    status.HTTP_404_NOT_FOUND: {
        "model": MensajeError,
        "description": "El registro no existe",
    },
}
RESPUESTA_409 = {
    status.HTTP_409_CONFLICT: {
        "model": MensajeError,
        "description": "Conflicto de integridad (registro duplicado o con "
                       "registros asociados)",
    },
}


def _crear_manejador(codigo: int):
    async def manejador(_request: Request, error: Exception) -> JSONResponse:
        return JSONResponse(status_code=codigo, content={"detail": str(error)})

    return manejador


def registrar_manejadores(app: FastAPI) -> None:
    """Registra en la app un manejador por cada error de negocio."""
    for excepcion, codigo in CODIGO_POR_EXCEPCION.items():
        app.add_exception_handler(excepcion, _crear_manejador(codigo))

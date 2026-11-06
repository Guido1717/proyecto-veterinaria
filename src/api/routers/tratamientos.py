"""Endpoints REST de la entidad Tratamiento."""
from fastapi import APIRouter, status

from src.api.dependencias import SesionDB
from src.api.errores import RESPUESTA_400, RESPUESTA_404
from src.crud import tratamiento_crud
from src.schemas.tratamiento import (
    TratamientoCreate,
    TratamientoRead,
    TratamientoUpdate,
)

router = APIRouter(prefix="/tratamientos", tags=["Tratamientos"])


@router.get(
    "/",
    response_model=list[TratamientoRead],
    status_code=status.HTTP_200_OK,
    summary="Listar tratamientos",
)
def listar_tratamientos(db: SesionDB):
    return tratamiento_crud.listar_tratamientos(db)


@router.get(
    "/{tratamiento_id}",
    response_model=TratamientoRead,
    status_code=status.HTTP_200_OK,
    summary="Obtener un tratamiento por id",
    responses=RESPUESTA_404,
)
def obtener_tratamiento(tratamiento_id: int, db: SesionDB):
    return tratamiento_crud.obtener_tratamiento(db, tratamiento_id)


@router.post(
    "/",
    response_model=TratamientoRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un tratamiento",
    responses=RESPUESTA_400,
)
def crear_tratamiento(datos: TratamientoCreate, db: SesionDB):
    return tratamiento_crud.crear_tratamiento(db, datos)


@router.put(
    "/{tratamiento_id}",
    response_model=TratamientoRead,
    status_code=status.HTTP_200_OK,
    summary="Actualizar un tratamiento",
    responses={**RESPUESTA_400, **RESPUESTA_404},
)
def actualizar_tratamiento(
    tratamiento_id: int, datos: TratamientoUpdate, db: SesionDB
):
    return tratamiento_crud.actualizar_tratamiento(db, tratamiento_id, datos)


@router.delete(
    "/{tratamiento_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar un tratamiento",
    responses=RESPUESTA_404,
)
def eliminar_tratamiento(tratamiento_id: int, db: SesionDB) -> None:
    tratamiento_crud.eliminar_tratamiento(db, tratamiento_id)

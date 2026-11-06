"""Endpoints REST de la entidad Veterinario."""
from fastapi import APIRouter, status

from src.api.dependencias import SesionDB
from src.api.errores import RESPUESTA_404, RESPUESTA_409
from src.crud import veterinario_crud
from src.schemas.veterinario import (
    VeterinarioCreate,
    VeterinarioRead,
    VeterinarioUpdate,
)

router = APIRouter(prefix="/veterinarios", tags=["Veterinarios"])


@router.get(
    "/",
    response_model=list[VeterinarioRead],
    status_code=status.HTTP_200_OK,
    summary="Listar veterinarios",
)
def listar_veterinarios(db: SesionDB):
    return veterinario_crud.listar_veterinarios(db)


@router.get(
    "/{veterinario_id}",
    response_model=VeterinarioRead,
    status_code=status.HTTP_200_OK,
    summary="Obtener un veterinario por id",
    responses=RESPUESTA_404,
)
def obtener_veterinario(veterinario_id: int, db: SesionDB):
    return veterinario_crud.obtener_veterinario(db, veterinario_id)


@router.post(
    "/",
    response_model=VeterinarioRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un veterinario",
)
def crear_veterinario(datos: VeterinarioCreate, db: SesionDB):
    return veterinario_crud.crear_veterinario(db, datos)


@router.put(
    "/{veterinario_id}",
    response_model=VeterinarioRead,
    status_code=status.HTTP_200_OK,
    summary="Actualizar un veterinario",
    responses=RESPUESTA_404,
)
def actualizar_veterinario(
    veterinario_id: int, datos: VeterinarioUpdate, db: SesionDB
):
    return veterinario_crud.actualizar_veterinario(db, veterinario_id, datos)


@router.delete(
    "/{veterinario_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar un veterinario",
    responses={**RESPUESTA_404, **RESPUESTA_409},
)
def eliminar_veterinario(veterinario_id: int, db: SesionDB) -> None:
    veterinario_crud.eliminar_veterinario(db, veterinario_id)

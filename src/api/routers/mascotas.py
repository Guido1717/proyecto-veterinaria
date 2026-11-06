"""Endpoints REST de la entidad Mascota."""
from fastapi import APIRouter, status

from src.api.dependencias import SesionDB
from src.api.errores import RESPUESTA_400, RESPUESTA_404, RESPUESTA_409
from src.crud import mascota_crud
from src.schemas.mascota import MascotaCreate, MascotaRead, MascotaUpdate

router = APIRouter(prefix="/mascotas", tags=["Mascotas"])


@router.get(
    "/",
    response_model=list[MascotaRead],
    status_code=status.HTTP_200_OK,
    summary="Listar mascotas",
)
def listar_mascotas(db: SesionDB):
    return mascota_crud.listar_mascotas(db)


@router.get(
    "/{mascota_id}",
    response_model=MascotaRead,
    status_code=status.HTTP_200_OK,
    summary="Obtener una mascota por id",
    responses=RESPUESTA_404,
)
def obtener_mascota(mascota_id: int, db: SesionDB):
    return mascota_crud.obtener_mascota(db, mascota_id)


@router.post(
    "/",
    response_model=MascotaRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear una mascota",
    responses=RESPUESTA_400,
)
def crear_mascota(datos: MascotaCreate, db: SesionDB):
    return mascota_crud.crear_mascota(db, datos)


@router.put(
    "/{mascota_id}",
    response_model=MascotaRead,
    status_code=status.HTTP_200_OK,
    summary="Actualizar una mascota",
    responses={**RESPUESTA_400, **RESPUESTA_404},
)
def actualizar_mascota(mascota_id: int, datos: MascotaUpdate, db: SesionDB):
    return mascota_crud.actualizar_mascota(db, mascota_id, datos)


@router.delete(
    "/{mascota_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar una mascota",
    responses={**RESPUESTA_404, **RESPUESTA_409},
)
def eliminar_mascota(mascota_id: int, db: SesionDB) -> None:
    mascota_crud.eliminar_mascota(db, mascota_id)

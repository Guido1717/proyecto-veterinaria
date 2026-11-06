"""Endpoints REST de la entidad Dueno."""
from fastapi import APIRouter, status

from src.api.dependencias import SesionDB
from src.api.errores import RESPUESTA_404, RESPUESTA_409
from src.crud import dueno_crud
from src.schemas.dueno import DuenoCreate, DuenoRead, DuenoUpdate

router = APIRouter(prefix="/duenos", tags=["Dueños"])


@router.get(
    "/",
    response_model=list[DuenoRead],
    status_code=status.HTTP_200_OK,
    summary="Listar dueños",
)
def listar_duenos(db: SesionDB):
    return dueno_crud.listar_duenos(db)


@router.get(
    "/{dueno_id}",
    response_model=DuenoRead,
    status_code=status.HTTP_200_OK,
    summary="Obtener un dueño por id",
    responses=RESPUESTA_404,
)
def obtener_dueno(dueno_id: int, db: SesionDB):
    return dueno_crud.obtener_dueno(db, dueno_id)


@router.post(
    "/",
    response_model=DuenoRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un dueño",
)
def crear_dueno(datos: DuenoCreate, db: SesionDB):
    return dueno_crud.crear_dueno(db, datos)


@router.put(
    "/{dueno_id}",
    response_model=DuenoRead,
    status_code=status.HTTP_200_OK,
    summary="Actualizar un dueño",
    responses=RESPUESTA_404,
)
def actualizar_dueno(dueno_id: int, datos: DuenoUpdate, db: SesionDB):
    return dueno_crud.actualizar_dueno(db, dueno_id, datos)


@router.delete(
    "/{dueno_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar un dueño",
    responses={**RESPUESTA_404, **RESPUESTA_409},
)
def eliminar_dueno(dueno_id: int, db: SesionDB) -> None:
    dueno_crud.eliminar_dueno(db, dueno_id)

"""Endpoints REST de la entidad Especie."""
from fastapi import APIRouter, status

from src.api.dependencias import SesionDB
from src.api.errores import RESPUESTA_404, RESPUESTA_409
from src.crud import especie_crud
from src.schemas.especie import EspecieCreate, EspecieRead, EspecieUpdate

router = APIRouter(prefix="/especies", tags=["Especies"])


@router.get(
    "/",
    response_model=list[EspecieRead],
    status_code=status.HTTP_200_OK,
    summary="Listar especies",
)
def listar_especies(db: SesionDB):
    return especie_crud.listar_especies(db)


@router.get(
    "/{especie_id}",
    response_model=EspecieRead,
    status_code=status.HTTP_200_OK,
    summary="Obtener una especie por id",
    responses=RESPUESTA_404,
)
def obtener_especie(especie_id: int, db: SesionDB):
    return especie_crud.obtener_especie(db, especie_id)


@router.post(
    "/",
    response_model=EspecieRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear una especie",
)
def crear_especie(datos: EspecieCreate, db: SesionDB):
    return especie_crud.crear_especie(db, datos)


@router.put(
    "/{especie_id}",
    response_model=EspecieRead,
    status_code=status.HTTP_200_OK,
    summary="Actualizar una especie",
    responses=RESPUESTA_404,
)
def actualizar_especie(especie_id: int, datos: EspecieUpdate, db: SesionDB):
    return especie_crud.actualizar_especie(db, especie_id, datos)


@router.delete(
    "/{especie_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar una especie",
    responses={**RESPUESTA_404, **RESPUESTA_409},
)
def eliminar_especie(especie_id: int, db: SesionDB) -> None:
    especie_crud.eliminar_especie(db, especie_id)

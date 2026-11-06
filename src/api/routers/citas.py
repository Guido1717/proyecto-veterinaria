"""Endpoints REST de la entidad Cita."""
from fastapi import APIRouter, status

from src.api.dependencias import SesionDB
from src.api.errores import RESPUESTA_400, RESPUESTA_404, RESPUESTA_409
from src.crud import cita_crud
from src.schemas.cita import CitaCreate, CitaRead, CitaUpdate

router = APIRouter(prefix="/citas", tags=["Citas"])


@router.get(
    "/",
    response_model=list[CitaRead],
    status_code=status.HTTP_200_OK,
    summary="Listar citas",
)
def listar_citas(db: SesionDB):
    return cita_crud.listar_citas(db)


@router.get(
    "/{cita_id}",
    response_model=CitaRead,
    status_code=status.HTTP_200_OK,
    summary="Obtener una cita por id",
    responses=RESPUESTA_404,
)
def obtener_cita(cita_id: int, db: SesionDB):
    return cita_crud.obtener_cita(db, cita_id)


@router.post(
    "/",
    response_model=CitaRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear una cita",
    responses=RESPUESTA_400,
)
def crear_cita(datos: CitaCreate, db: SesionDB):
    return cita_crud.crear_cita(db, datos)


@router.put(
    "/{cita_id}",
    response_model=CitaRead,
    status_code=status.HTTP_200_OK,
    summary="Actualizar una cita",
    responses={**RESPUESTA_400, **RESPUESTA_404},
)
def actualizar_cita(cita_id: int, datos: CitaUpdate, db: SesionDB):
    return cita_crud.actualizar_cita(db, cita_id, datos)


@router.delete(
    "/{cita_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar una cita",
    responses={**RESPUESTA_404, **RESPUESTA_409},
)
def eliminar_cita(cita_id: int, db: SesionDB) -> None:
    cita_crud.eliminar_cita(db, cita_id)

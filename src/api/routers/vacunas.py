"""Endpoints REST de la entidad Vacuna."""
from fastapi import APIRouter, status

from src.api.dependencias import SesionDB
from src.api.errores import RESPUESTA_400, RESPUESTA_404
from src.crud import vacuna_crud
from src.schemas.vacuna import VacunaCreate, VacunaRead, VacunaUpdate

router = APIRouter(prefix="/vacunas", tags=["Vacunas"])


@router.get(
    "/",
    response_model=list[VacunaRead],
    status_code=status.HTTP_200_OK,
    summary="Listar vacunas",
)
def listar_vacunas(db: SesionDB):
    return vacuna_crud.listar_vacunas(db)


@router.get(
    "/{vacuna_id}",
    response_model=VacunaRead,
    status_code=status.HTTP_200_OK,
    summary="Obtener una vacuna por id",
    responses=RESPUESTA_404,
)
def obtener_vacuna(vacuna_id: int, db: SesionDB):
    return vacuna_crud.obtener_vacuna(db, vacuna_id)


@router.post(
    "/",
    response_model=VacunaRead,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar una vacuna",
    responses=RESPUESTA_400,
)
def crear_vacuna(datos: VacunaCreate, db: SesionDB):
    return vacuna_crud.crear_vacuna(db, datos)


@router.put(
    "/{vacuna_id}",
    response_model=VacunaRead,
    status_code=status.HTTP_200_OK,
    summary="Actualizar una vacuna",
    responses={**RESPUESTA_400, **RESPUESTA_404},
)
def actualizar_vacuna(vacuna_id: int, datos: VacunaUpdate, db: SesionDB):
    return vacuna_crud.actualizar_vacuna(db, vacuna_id, datos)


@router.delete(
    "/{vacuna_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar una vacuna",
    responses=RESPUESTA_404,
)
def eliminar_vacuna(vacuna_id: int, db: SesionDB) -> None:
    vacuna_crud.eliminar_vacuna(db, vacuna_id)

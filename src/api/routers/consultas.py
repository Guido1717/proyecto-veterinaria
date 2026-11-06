"""Endpoints REST de la entidad Consulta."""
from fastapi import APIRouter, status

from src.api.dependencias import SesionDB
from src.api.errores import RESPUESTA_400, RESPUESTA_404, RESPUESTA_409
from src.crud import consulta_crud
from src.schemas.consulta import ConsultaCreate, ConsultaRead, ConsultaUpdate

router = APIRouter(prefix="/consultas", tags=["Consultas"])


@router.get(
    "/",
    response_model=list[ConsultaRead],
    status_code=status.HTTP_200_OK,
    summary="Listar consultas",
)
def listar_consultas(db: SesionDB):
    return consulta_crud.listar_consultas(db)


@router.get(
    "/{consulta_id}",
    response_model=ConsultaRead,
    status_code=status.HTTP_200_OK,
    summary="Obtener una consulta por id",
    responses=RESPUESTA_404,
)
def obtener_consulta(consulta_id: int, db: SesionDB):
    return consulta_crud.obtener_consulta(db, consulta_id)


@router.post(
    "/",
    response_model=ConsultaRead,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar una consulta",
    description="Registra la consulta de una cita y cambia la cita a "
                "estado 'atendida'. Una cita admite una sola consulta.",
    responses={**RESPUESTA_400, **RESPUESTA_409},
)
def crear_consulta(datos: ConsultaCreate, db: SesionDB):
    return consulta_crud.crear_consulta(db, datos)


@router.put(
    "/{consulta_id}",
    response_model=ConsultaRead,
    status_code=status.HTTP_200_OK,
    summary="Actualizar una consulta",
    responses=RESPUESTA_404,
)
def actualizar_consulta(consulta_id: int, datos: ConsultaUpdate, db: SesionDB):
    return consulta_crud.actualizar_consulta(db, consulta_id, datos)


@router.delete(
    "/{consulta_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar una consulta",
    responses={**RESPUESTA_404, **RESPUESTA_409},
)
def eliminar_consulta(consulta_id: int, db: SesionDB) -> None:
    consulta_crud.eliminar_consulta(db, consulta_id)

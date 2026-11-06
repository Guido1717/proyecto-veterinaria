"""Clases base compartidas por los schemas de todas las entidades."""
from pydantic import BaseModel, ConfigDict, model_validator


class CreacionBase(BaseModel):
    """Base de los schemas Create: quita espacios sobrantes en los textos."""

    model_config = ConfigDict(str_strip_whitespace=True)


class ActualizacionBase(BaseModel):
    """Base de los schemas Update.

    Todos los campos son opcionales: solo se modifican los que se envían.
    Enviar un campo con valor null no está permitido.
    """

    model_config = ConfigDict(str_strip_whitespace=True)

    @model_validator(mode="after")
    def rechazar_nulos(self):
        nulos = sorted(
            campo for campo in self.model_fields_set
            if getattr(self, campo) is None
        )
        if nulos:
            raise ValueError(
                "Estos campos no pueden ser null: " + ", ".join(nulos)
            )
        return self


class LecturaBase(BaseModel):
    """Base de los schemas Read: se construyen desde objetos del ORM."""

    model_config = ConfigDict(from_attributes=True)

    id: int

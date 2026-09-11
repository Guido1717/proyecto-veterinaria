from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from src.database.connection import Base


class Especie(Base):
    __tablename__ = "especies"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(200), default="")

    mascotas = relationship("Mascota", back_populates="especie")


class Dueno(Base):
    __tablename__ = "duenos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    telefono = Column(String(20), nullable=False)
    direccion = Column(String(200), default="")

    mascotas = relationship("Mascota", back_populates="dueno")


class Mascota(Base):
    __tablename__ = "mascotas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    edad = Column(Integer, nullable=False)
    especie_id = Column(Integer, ForeignKey("especies.id"), nullable=False)
    dueno_id = Column(Integer, ForeignKey("duenos.id"), nullable=False)

    especie = relationship("Especie", back_populates="mascotas")
    dueno = relationship("Dueno", back_populates="mascotas")
    citas = relationship("Cita", back_populates="mascota")
    vacunas = relationship("Vacuna", back_populates="mascota")


class Veterinario(Base):
    __tablename__ = "veterinarios"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    especialidad = Column(String(100), nullable=False)
    telefono = Column(String(20), nullable=False)

    citas = relationship("Cita", back_populates="veterinario")


class Cita(Base):
    __tablename__ = "citas"

    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    estado = Column(String(20), default="pendiente")
    mascota_id = Column(Integer, ForeignKey("mascotas.id"), nullable=False)
    veterinario_id = Column(Integer, ForeignKey("veterinarios.id"), nullable=False)

    mascota = relationship("Mascota", back_populates="citas")
    veterinario = relationship("Veterinario", back_populates="citas")
    consulta = relationship("Consulta", back_populates="cita", uselist=False)


class Consulta(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True)
    diagnostico = Column(String(300), nullable=False)
    observaciones = Column(String(300), default="")
    cita_id = Column(Integer, ForeignKey("citas.id"), nullable=False)

    cita = relationship("Cita", back_populates="consulta")
    tratamientos = relationship("Tratamiento", back_populates="consulta")


class Vacuna(Base):
    __tablename__ = "vacunas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    fecha_aplicacion = Column(Date, nullable=False)
    mascota_id = Column(Integer, ForeignKey("mascotas.id"), nullable=False)

    mascota = relationship("Mascota", back_populates="vacunas")


class Tratamiento(Base):
    __tablename__ = "tratamientos"

    id = Column(Integer, primary_key=True)
    medicamento = Column(String(100), nullable=False)
    duracion_dias = Column(Integer, nullable=False)
    consulta_id = Column(Integer, ForeignKey("consultas.id"), nullable=False)

    consulta = relationship("Consulta", back_populates="tratamientos")
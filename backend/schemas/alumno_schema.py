from pydantic import BaseModel, EmailStr  # BaseModel para crear esquemas Pydantic, EmailStr para validar correos electrónicos
from typing import Optional  # Permite definir campos opcionales

# Esquema base con los campos comunes de un alumno
class AlumnoBase(BaseModel):
    nombre: str
    correo: EmailStr
    carrera: str
    semestre: int

# Esquema para crear un alumno, hereda de AlumnoBase
class AlumnoCreate(AlumnoBase):
    pass  # Igual que base

# Esquema para actualizar un alumno, todos los campos son opcionales
class AlumnoUpdate(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[EmailStr] = None
    carrera: Optional[str] = None
    semestre: Optional[int] = None

# Esquema de salida para mostrar un alumno, incluye el ID
class AlumnoOut(AlumnoBase):
    id: int

    class Config:
        from_attributes = True  # Permite que Pydantic trabaje con objetos ORM de SQLAlchemy en Pydantic v2

# Un esquema Pydantic es una forma de definir la estructura de los datos que se esperan en las solicitudes y respuestas de la API, asegurando que cumplan con ciertos requisitos y tipos.


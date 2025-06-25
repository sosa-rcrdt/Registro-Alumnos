from sqlalchemy import Column, Integer, String  # Importa tipos de columna y tipos de datos para el modelo
from database import Base  # Importa la clase base para definir modelos ORM

# Modelo Alumno que representa la tabla 'alumnos' en la base de datos
class Alumno(Base):
    __tablename__ = "alumnos"  # Nombre de la tabla en la base de datos

    id = Column(Integer, primary_key = True, index = True)  # Columna ID, clave primaria y con índice
    nombre = Column(String(100), nullable = False)  # Columna para el nombre del alumno, no puede ser nulo
    correo = Column(String(100), nullable = False, unique = True)  # Columna para el correo, único y no nulo
    carrera = Column(String(50), nullable = False)  # Columna para la carrera, no puede ser nulo
    semestre = Column(Integer, nullable = False)  # Columna para el semestre, no puede ser nulo


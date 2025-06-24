from fastapi import APIRouter, Depends, HTTPException  # APIRouter para definir rutas, Depends para inyección de dependencias, HTTPException para manejar errores HTTP
from sqlalchemy.orm import Session  # Importa la clase Session para interactuar con la base de datos
from database import SessionLocal  # Importa la clase de sesión configurada para la base de datos
from models.alumno import Alumno  # Importa el modelo Alumno

# Define un router para agrupar las rutas relacionadas con alumnos, esto para organizar mejor el código
router = APIRouter(prefix="/alumnos", tags=["alumnos"])

# Dependencia para obtener una sesión de base de datos y cerrarla automáticamente
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# El try y el finally aseguran que la sesión se cierre correctamente después de su uso.

# Endpoint para obtener todos los alumnos
@router.get("/") # Se pone "/" para indicar que es el endpoint raíz de este router
def obtener_alumnos(db: Session = Depends(get_db)): # Dependencia para la sesión de base de datos
    return db.query(Alumno).all() # Obtiene todos los registros de la tabla Alumno

# Endpoint para crear un nuevo alumno
@router.post("/") # Se pone "/" para indicar que es el endpoint raíz de este router
def crear_alumno(alumno: dict, db: Session = Depends(get_db)): # Recibe un diccionario con los datos del alumno y una sesión de base de datos
    nuevo = Alumno(**alumno) # Crea una instancia del modelo Alumno usando los datos recibidos
    db.add(nuevo) # Añade el nuevo alumno a la sesión de base de datos
    db.commit() # Guarda los cambios en la base de datos
    db.refresh(nuevo) # Refresca el objeto nuevo para obtener los datos actualizados desde la base de datos
    return nuevo # Devuelve el nuevo alumno creado


from fastapi import APIRouter, Depends, HTTPException  # APIRouter para definir rutas, Depends para inyección de dependencias, HTTPException para manejar errores HTTP
from sqlalchemy.orm import Session  # Importa la clase Session para interactuar con la base de datos
from database import SessionLocal  # Importa la clase de sesión configurada para la base de datos
from models.alumno import Alumno  # Importa el modelo Alumno
from schemas.alumno_schema import AlumnoCreate, AlumnoUpdate, AlumnoOut  # Importa los esquemas Pydantic

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
@router.get("/", response_model=list[AlumnoOut])  # Devuelve una lista de alumnos con el esquema de salida
def obtener_alumnos(db: Session = Depends(get_db)):
    return db.query(Alumno).all()

# Endpoint para crear un nuevo alumno
@router.post("/", response_model=AlumnoOut)
def crear_alumno(alumno: AlumnoCreate, db: Session = Depends(get_db)):
    nuevo = Alumno(**alumno.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# Endpoint para editar un alumno existente
@router.put("/{alumno_id}", response_model=AlumnoOut)
def actualizar_alumno(alumno_id: int, alumno_data: AlumnoUpdate, db: Session = Depends(get_db)):
    alumno = db.query(Alumno).filter(Alumno.id == alumno_id).first()
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    # Actualiza solo los campos enviados en la petición
    for key, value in alumno_data.dict(exclude_unset=True).items():
        setattr(alumno, key, value)
    db.commit()
    db.refresh(alumno)  # Refresca el objeto para obtener los datos actualizados
    return alumno  # Devuelve el alumno actualizado

# Endpoint para eliminar un alumno
@router.delete("/{alumno_id}")
def eliminar_alumno(alumno_id: int, db: Session = Depends(get_db)):
    alumno = db.query(Alumno).filter(Alumno.id == alumno_id).first()
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    db.delete(alumno)  # Elimina el alumno de la base de datos
    db.commit()  # Guarda los cambios en la base de datos
    return {"mensaje": "Alumno eliminado"}  # Devuelve un mensaje de confirmación


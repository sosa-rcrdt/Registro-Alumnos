from fastapi import FastAPI # Importa FastAPI para crear la aplicación web
from database import engine, Base  # Importa la configuración de la base de datos y los modelos
from routers import alumno_router  # Importa las rutas (endpoints) de alumnos

# Inicializa la aplicación FastAPI
app = FastAPI()

# Crea automáticamente las tablas en la base de datos según los modelos definidos (solo recomendable en desarrollo)
Base.metadata.create_all(bind=engine)

# Incluye las rutas definidas en el router de alumnos
app.include_router(alumno_router.router)

# Ruta raíz para verificar que la API está activa
@app.get("/")
def read_root():
    return {"message": "API de Registro de Alumnos activa"}


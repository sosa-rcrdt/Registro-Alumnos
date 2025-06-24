from fastapi import FastAPI # Importa FastAPI para crear la aplicación web
from fastapi.middleware.cors import CORSMiddleware  # Importa el middleware de CORS
from database import engine, Base  # Importa la configuración de la base de datos y los modelos
from routers import alumno_router  # Importa las rutas (endpoints) de alumnos

# Inicializa la aplicación FastAPI
app = FastAPI()

# Configura el middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",      # React por defecto
        "http://localhost:5173",      # Vue + Vite por defecto
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todas las cabeceras
)

# Crea automáticamente las tablas en la base de datos según los modelos definidos (solo recomendable en desarrollo)
Base.metadata.create_all(bind=engine)

# Incluye las rutas definidas en el router de alumnos
app.include_router(alumno_router.router)

# Ruta raíz para verificar que la API está activa
@app.get("/")
def read_root():
    return {"message": "API de Registro de Alumnos activa"}


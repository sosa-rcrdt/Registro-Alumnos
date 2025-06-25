from database import Base, engine
from models.alumno import Alumno  # Asegúrate de importar todos tus modelos aquí

print("Creando las tablas en la base de datos...")
Base.metadata.create_all(bind=engine)
print("Listo.")

# Este script se encarga de inicializar la base de datos creando las tablas definidas en los modelos.
# Se separa del archivo main.py para mantener una estructura limpia y modular.


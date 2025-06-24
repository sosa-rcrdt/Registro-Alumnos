import os  # Permite acceder a variables de entorno del sistema operativo
from sqlalchemy import create_engine  # Crea el motor de conexión a la base de datos
from sqlalchemy.orm import sessionmaker, declarative_base  # sessionmaker: crea sesiones para interactuar con la BD; declarative_base: clase base para modelos ORM
from dotenv import load_dotenv  # Carga variables de entorno desde un archivo .env

# Carga las variables de entorno definidas en el archivo .env
load_dotenv()

# Obtiene los datos de conexión a la base de datos desde las variables de entorno
server = os.getenv("DB_SERVER")
database = os.getenv("DB_DATABASE")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

# Construye la cadena de conexión para SQL Server usando el driver ODBC
connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"

# Crea el motor de conexión a la base de datos
engine = create_engine(connection_string)

# Crea una clase de sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autoflush=False, bind=engine)

# Clase base para definir los modelos ORM (tablas)
Base = declarative_base()


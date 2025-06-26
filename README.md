# Sistema de Registro de Alumnos

Este proyecto es una aplicación **FullStack** desarrollada con **Vue 3 + Tailwind CSS** en el frontend y **FastAPI + SQL Server** en el backend. Permite registrar, editar, consultar y eliminar alumnos de una base de datos de forma amigable e intuitiva.

---

## 📁 Estructura del Proyecto

```
.
├── backend/          # Backend con FastAPI y conexión a SQL Server
│   ├── models/       # Modelos de base de datos (SQLAlchemy)
│   ├── routers/      # Rutas de la API
│   ├── schemas/      # Esquemas de validación Pydantic
│   ├── init_db.py    # Script para inicializar la base de datos
│   ├── main.py       # Punto de entrada del backend
│   └── database.py   # Configuración de la base de datos
│
├── frontend/         # Frontend con Vue 3 y Tailwind CSS
│   ├── src/          
│   │   ├── components/  # Componentes reutilizables
│   │   ├── views/       # Vistas (pantallas) principales
│   │   └── router/      # Configuración de rutas con Vue Router
│   └── vite.config.js
│
├── .gitignore
├── .gitattributes
└── README.md         # Este archivo
```

---

## Requisitos

- Node.js >= 18
- Python 3.10+
- SQL Server
- Driver ODBC 17 for SQL Server
- Navegador moderno (Chrome, Firefox, etc.)

---

## Instalación y ejecución

### Backend (FastAPI)

1. Entra a la carpeta del backend:
   ```bash
   cd backend
   ```

2. Crea un entorno virtual y actívalo:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Crea un archivo `.env` con tu configuración de base de datos:
   ```
   DB_SERVER=localhost
   DB_DATABASE=nombre_de_tu_bd
   DB_USERNAME=usuario
   DB_PASSWORD=contraseña
   ```

5. Inicializa la base de datos:
   ```bash
   python init_db.py
   ```

6. Ejecuta el servidor:
   ```bash
   uvicorn main:app --reload
   ```

7. Visita la documentación en: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### Frontend (Vue 3)

1. En otra terminal, entra a la carpeta del frontend:
   ```bash
   cd frontend
   ```

2. Instala dependencias:
   ```bash
   npm install
   ```

3. Ejecuta el servidor de desarrollo:
   ```bash
   npm run dev
   ```

4. Accede a la app en: [http://localhost:5173](http://localhost:5173)

---

## Funcionalidades

- Listar alumnos registrados
- Añadir nuevo alumno
- Editar datos de un alumno existente
- Eliminar alumno con confirmación (modal animado)
- Validación de campos
- Diseño responsivo y agradable con Tailwind CSS
- Comunicación asincrónica con Axios

---

## Tecnologías utilizadas

- **Frontend:** Vue 3, Vite, Tailwind CSS, Vue Router, Axios
- **Backend:** FastAPI, SQLAlchemy, Pydantic, Python 3.10
- **Base de Datos:** SQL Server (via pyodbc)

---

## Autor

Desarrollado por Nelson Ricardo Sosa Francisco.
Este proyecto ha sido desarrollado de manera personal e independiente como ejercicio práctico para aplicar y consolidar conocimientos en desarrollo FullStack con tecnologías modernas como FastAPI, Vue 3, Tailwind CSS y SQL Server.
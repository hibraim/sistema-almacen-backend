from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from .database import init_db
from . import routers

app = FastAPI(title="Sistema SPM Almacén", version="3.2")

# Configuración de permisos para que React se comunique sin bloqueos
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carpeta para guardar las fotos de los artículos
os.makedirs("static/uploads", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Iniciar la base de datos al arrancar
@app.on_event("startup")
def startup_event():
    init_db()

# ¡AQUÍ ESTÁ LA MAGIA! Conectamos todas las rutas de guardado, edición y eliminación
app.include_router(routers.router)

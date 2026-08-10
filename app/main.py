from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from app.routers import router as api_router
from app.database import init_db

app = FastAPI()

# Configuración de CORS para conectar con Vercel y celulares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carpeta para archivos estáticos
os.makedirs("static/uploads", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Inicializar base de datos
@app.on_event("startup")
def startup_event():
    init_db()

# Incluir rutas con el prefijo limpio
app.include_router(api_router)

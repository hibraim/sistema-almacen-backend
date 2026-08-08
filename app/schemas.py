from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class ProductoCreate(BaseModel):
    codigo_interno: str
    codigo_barras: Optional[str] = None
    nombre: str
    descripcion: Optional[str] = None
    categoria_id: int
    unidad_medida: str = "Pieza"
    stock_actual: Decimal = 0
    stock_minimo: Decimal = 0
    stock_maximo: Decimal = 0
    observaciones: Optional[str] = None

class ProductoOut(ProductoCreate):
    id: str
    imagen_principal: Optional[str] = None
    activo: bool

    class Config:
        from_attributes = True

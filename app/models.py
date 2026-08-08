from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    descripcion = Column(String, nullable=True)

class Area(Base):
    __tablename__ = "areas"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    encargado = Column(String)
    cargo = Column(String, default="Director")

class SubArea(Base):
    __tablename__ = "subareas"
    id = Column(Integer, primary_key=True, index=True)
    area_id = Column(Integer, ForeignKey("areas.id"))
    nombre = Column(String)
    encargado = Column(String)
    cargo = Column(String, default="Jefe")

class Producto(Base):
    __tablename__ = "productos"
    id = Column(String, primary_key=True, index=True)
    codigo_interno = Column(String, unique=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String, nullable=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    stock_actual = Column(Integer, default=0)
    stock_minimo = Column(Integer, default=5)
    stock_maximo = Column(Integer, default=1000)
    unidad_medida = Column(String, default="Pieza")
    imagen_principal = Column(String, nullable=True)

class Entrada(Base):
    __tablename__ = "entradas"
    id = Column(String, primary_key=True, index=True)
    folio = Column(String, index=True)
    fecha = Column(DateTime, default=datetime.utcnow)
    producto_id = Column(String, ForeignKey("productos.id"))
    cantidad = Column(Integer)
    area_id = Column(Integer, ForeignKey("areas.id"), nullable=True)
    proveedor = Column(String, nullable=True)
    recibio_nombre = Column(String, nullable=True)
    entrego_nombre = Column(String, nullable=True)

class Salida(Base):
    __tablename__ = "salidas"
    id = Column(String, primary_key=True, index=True)
    folio = Column(String, index=True)
    fecha = Column(DateTime, default=datetime.utcnow)
    producto_id = Column(String, ForeignKey("productos.id"))
    cantidad = Column(Integer)
    area_id = Column(Integer, ForeignKey("areas.id"), nullable=True)
    subarea_id = Column(Integer, ForeignKey("subareas.id"), nullable=True)
    descripcion = Column(String, nullable=True)
    recibio_nombre = Column(String, nullable=True)
    entrego_nombre = Column(String, nullable=True)

class User(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    nombre = Column(String)
    rol = Column(String)

from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from inventario.bd import Base

class Producto(Base):
    __tablename__ = 'productos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    precio = Column(Float, nullable=False)
    cantidad = Column(Integer, default=0)
    email_proveedor = Column(String(120), nullable=True)
    fecha_registro = Column(DateTime, default=datetime.utcnow)

from app.db.database import Base
from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = 'usuario'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username=Column(String,unique=True)
    password=Column(String)
    nombre = Column(String)
    apellido = Column(String)
    direccion = Column(String)
    telefono = Column(Integer)
    correo = Column(String,unique=True)
    creacion = Column(DateTime,default=datetime.now,onupdate=datetime.now)
    estado = Column(Boolean,default=False)
    venta=relationship("Venta",backref="usuario", cascade="delete,merge")

class Venta(Base):
    __tablename__="venta"
    id=Column(Integer, primary_key=True,autoincrement=True)
    usuario_id=Column(Integer,ForeignKey('usuario.id'))
    producto_id = Column(Integer, ForeignKey('producto.id'))
    producto_venta = relationship("Producto", backref="venta_producto")
    ventas_productos=Column(Integer)

class Producto(Base):
    __tablename__="producto"
    id=Column(Integer, primary_key=True,autoincrement=True)
    nombre=Column(String)
    descripcion=Column(String)
    precio=Column(String)
    stock=Column(String)  
    ventas=relationship("Venta", backref="producto")  

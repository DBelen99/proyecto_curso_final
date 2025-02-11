from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#User Model
class User(BaseModel): #Schema
    id:int
    username:str 
    password:str 
    nombre:str
    apellido:str
    direccion:Optional[str] #Parámetro opcional; es necesario importar Optional
    telefono:int
    correo:str
    creacion_user:datetime=datetime.now() #Fecha por defecto
    


class Venta(BaseModel):  
    id:int
    usuario_id:int  
    producto_id:int
    venta:int
    ventas_productos:int

class Producto(BaseModel):  
    id:int
    nombre:str
    descripcion:str 
    precio:int
    stock:int

class UpdateUser(BaseModel):
    username:str = None
    password:str = None
    nombre:str = None
    apellido:str = None
    direccion:str = None #Parámetro opcional; es necesario importar Optional
    telefono:int = None
    correo:str = None
    

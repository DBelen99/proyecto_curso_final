from fastapi import APIRouter,Depends
from app.schemas import Producto
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models

productos = []

router = APIRouter(
    prefix="/producto",
    tags=["Productos"]
)

# @router.get("/ruta1")
# def ruta1():
#     return{"mensaje": "Hemos creado nuestra primera API!!!"}

@router.get("")
def obtener_productos(db:Session=Depends(get_db)):
    data = db.query(models.Producto).all()
    print(data)
    return productos

@router.post("")
def crear_producto(producto:Producto):
    producto = producto.model_dump()
    productos.append(producto)
    return {"Respuesta": "Producto creado!"}

@router.post("/{producto_id}")
def obtener_producto(producto_id:int):
    for producto in productos:
        if producto["id"] == producto_id: 
            return {"producto":producto}
    return{"respuesta": "Producto no encontrado"} 

# @router.post("json")
# def obtener_usuario_json(user_id:UserId):
#     for user in usuarios:
#         if user["id"] == user_id.id: 
#             return{"usuario":user}
#     return{"respuesta": "Usuario no encontrado"} 

@router.delete("/{producto_id}")
def eliminar_producto(producto_id:int):
    for index,producto in enumerate(productos):
        if producto["id"] == producto_id:
            productos.pop(index)
            return {"Respuesta": "Producto eliminado correctamente"}
    return {"Respuesta": "Producto NO encontrado"}

@router.put("/{producto_id}")
def actualizar_producto(producto_id:int, updateProducto:Producto):
    for index, producto in enumerate(productos): 
        if producto["id"] == producto_id:
            productos[index]["id"] = updateProducto.model_dump()["id"]
            productos[index]["nombre"] = updateProducto.model_dump()["nombre"]
            productos[index]["descripcion"] = updateProducto.model_dump()["descripcion"]
            productos[index]["precio"] = updateProducto.model_dump()["precio"]
            productos[index]["stock"] = updateProducto.model_dump()["stock"]
            productos[index]["ventas"] = updateProducto.model_dump()["ventas"]
            return {"Respuesta": "Producto actualizado correctamente"}
        return {"Respuesta": "Producto NO encontrado"}

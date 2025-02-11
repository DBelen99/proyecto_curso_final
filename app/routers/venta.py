from fastapi import APIRouter,Depends
from app.schemas import Venta
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models

ventas = []

router = APIRouter(
    prefix="/venta",
    tags=["Ventas"]
)


@router.get("")
def obtener_ventas(db:Session=Depends(get_db)):
    data = db.query(models.Venta).all()
    print(data)
    return ventas

@router.post("")
def crear_venta(venta:Venta):
    venta = venta.model_dump()
    ventas.append(venta)
    return {"Respuesta": "Venta creada!"}

@router.post("/{venta_id}")
def obtener_venta(venta_id:int):
    for venta in ventas:
        if venta["id"] == venta_id: 
            return {"venta":venta}
    return{"respuesta": "Venta no encontrada"} 


@router.delete("/{venta_id}")
def eliminar_venta(venta_id:int):
    for index,venta in enumerate(ventas): 
        if venta["id"] == venta_id:
            ventas.pop(index)
            return {"Respuesta": "Venta eliminada correctamente"}
    return {"Respuesta": "Venta NO encontrada"}

@router.put("/{venta_id}")
def actualizar_venta(venta_id:int, updateVenta:Venta):
    for index, user in enumerate(ventas): 
        if user["id"] == venta_id:
            ventas[index]["id"] = updateVenta.model_dump()["id"]
            ventas[index]["usuario_id"] = updateVenta.model_dump()["usuario_id"]
            ventas[index]["producto_id"] = updateVenta.model_dump()["producto_id"]
            ventas[index]["venta"] = updateVenta.model_dump()["venta"]
            ventas[index]["ventas_productos"] = updateVenta.model_dump()["venta_productos"]
            return {"Respuesta": "Venta actualizada correctamente"}
        return {"Respuesta": "Venta NO encontrada"}

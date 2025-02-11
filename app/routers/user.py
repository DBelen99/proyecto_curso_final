from fastapi import APIRouter,Depends
from app.schemas import User, UpdateUser
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models

usuarios = []

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.get("")
def obtener_usuarios(db:Session=Depends(get_db)):
    data = db.query(models.User).all()
    print(data)
    return data

@router.post("")
def crear_usuario(user:User, db:Session=Depends(get_db)):
    usuario=user.model_dump()
    nuevo_usuario=models.User(
        username=usuario["username"],
        password=usuario["password"],
        nombre=usuario["nombre"],
        apellido=usuario["apellido"],
        direccion=usuario["direccion"],
        telefono=usuario["telefono"],
        correo=usuario["correo"],
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return{"Respuesta": "Usuario creado!!"}

@router.get("/{user_id}")
def obtener_usuario(user_id:int, db:Session=Depends(get_db)):
    usuario=db.query(models.User).filter(models.User.id==user_id).first()
    if not usuario:
        return{"respuesta": "Usuario no encontrado"} #Si se pasa un id de un usuario que no existe
    return usuario


@router.delete("/{user_id}")
def eliminar_usuario(user_id: int, db: Session = Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.id == user_id).first()
    if not usuario:
        return {"respuesta": "Usuario no encontrado"}
    db.delete(usuario)
    db.commit()
    return {"Respuesta": "Usuario eliminado correctamente"}

@router.patch("/{user_id}")
def actualizar_usuario(user_id:int, updateUser:UpdateUser, db:Session=Depends(get_db)):
    usuario=db.query(models.User).filter(models.User.id==user_id)
    if not usuario.first():
        return{"respuesta": "Usuario no encontrado"}
    usuario.update(updateUser.model_dump(exclude_unset=True))
    db.commit()
    return{"Respesuta":"Usuario actualizado correctamente"}
   

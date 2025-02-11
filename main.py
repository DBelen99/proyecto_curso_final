from fastapi import FastAPI
import uvicorn
from app.routers import user, venta, producto
from app.db.database import Base, engine

def create_tables():
    Base.metadata.create_all(bind=engine)

create_tables()


app = FastAPI()
app.include_router(user.router)
app.include_router(venta.router)
app.include_router(producto.router)

if __name__=="__main__":
    uvicorn.run("main:app", port=8000, reload=True)
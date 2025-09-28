from fastapi import FastAPI
from database import Base, engine
from routers import users

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Reservas - LaForja")

# Rutas
app.include_router(users.router)

@app.get("/")
def root():
    return {"mensaje": "API LaForja funcionando 🚀"}

from fastapi import FastAPI
from database import Base, engine
from routers import users
from fastapi.middleware.cors import CORSMiddleware
from routers.register import router as register_router

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Reservas - LaForja")

origins = [
    # Permite el acceso desde el mismo origen de la documentación
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    # Puedes añadir otros dominios o puertos que uses, si es necesario
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,                     # Lista de orígenes permitidos
    allow_credentials=True,                    # Permite cookies de origen cruzado (si aplica)
    allow_methods=["*"],                       # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],                       # Permite todos los encabezados
)


# Rutas
app.include_router(users.router)
app.include_router(register_router)
@app.get("/")
def root():
    return {"mensaje": "API LaForja funcionando 🚀"}

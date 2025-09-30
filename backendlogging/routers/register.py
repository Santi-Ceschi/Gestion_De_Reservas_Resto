from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import Usuario
from routers.schemas import UserCreate, UserOut
from passlib.context import CryptContext

router = APIRouter(prefix="/users", tags=["Usuarios"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(Usuario).filter(Usuario.email == user.email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El email ya está registrado")

    user_bytes = user.contrasena.encode("utf-8")[:72]
    user.contrasena = user_bytes.decode("utf-8", errors="ignore")
    hashed_password = pwd_context.hash(user.contrasena)
    nuevo_usuario = Usuario(
        nombre=user.nombre,
        email=str(user.email),
        telefono=user.telefono,
        direccion=user.direccion,
        contrasena=hashed_password,
        rol=user.rol
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

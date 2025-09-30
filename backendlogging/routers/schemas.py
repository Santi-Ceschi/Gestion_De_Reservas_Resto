from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    nombre: str
    email: EmailStr
    telefono: str
    direccion: str
    contrasena: str
    rol: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id_usuario: int
    nombre: str
    email: EmailStr
    rol: str

    class Config:
        orm_mode = True

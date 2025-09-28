from pydantic import BaseModel, EmailStr

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

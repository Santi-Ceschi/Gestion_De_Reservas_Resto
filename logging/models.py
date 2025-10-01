from sqlalchemy import Column, Integer, String, Enum
from database import Base

class Usuario(Base):
    __tablename__ = "Usuario"

    id_usuario = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    telefono = Column(String(20))
    direccion = Column(String(200))
    contrasena = Column(String(200), nullable=False)  # Contraseña hasheada
    rol = Column(Enum("cliente", "administrador", name="rol_enum"), default="cliente", nullable=False)


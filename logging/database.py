from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root2:123456@localhost:3306/LaForja"

engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependencia de sesión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

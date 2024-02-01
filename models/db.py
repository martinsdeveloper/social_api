from sqlalchemy import Column, Integer, String, create_engine, UniqueConstraint
from sqlalchemy_utils import PasswordType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine(os.environ.get("SQLALCHEMY_DATABASE_URL", "sqlite:///./test.db"))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    salt = Column(String)
    password = Column(PasswordType(schemes=['bcrypt']))

    __table_args__ = (
        UniqueConstraint('full_name', name='uq_full_name'),
    )

Base.metadata.create_all(bind=engine)

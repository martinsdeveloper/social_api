import importlib.util
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
import os


def import_class_from_file(file_path, class_name):
    spec = importlib.util.spec_from_file_location("module_name", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    imported_class = getattr(module, class_name)
    return imported_class

engine = create_engine(os.environ.get("SQLALCHEMY_DATABASE_URL", 'sqlite:///./test.db'))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

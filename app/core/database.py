from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.core.config import settings

# create engine
engine = create_engine(settings.DATABASE_URL, echo=True)

# create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create base class for models
class Base(DeclarativeBase):
    pass
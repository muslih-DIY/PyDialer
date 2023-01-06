from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from fastapi import Request

#DATABASE_URL = "sqlite:///./database.db"

# DATABASE_URL = "postgresql://user:password@postgresserver/db"
DATABASE_URL = "postgresql://AsteriskPBX:PyPbX-secret@localhost:5432/PYPBX-RDB"
engin = create_engine(DATABASE_URL)

session:Session = sessionmaker(bind=engin,autoflush=False,autocommit=False)

# Dependency
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

async def update_db(request: Request):
    db:Session = next(get_db())
    setattr(request,'db',db)

    
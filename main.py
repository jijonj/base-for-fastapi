from fastapi import FastAPI
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from app.routers import user
from app.dependencies import get_db, Base
from app.config import settings

# Database setup
DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# FastAPI application instance
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Including routers
app.include_router(user.router)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}

# You can add more routers or additional configurations as needed

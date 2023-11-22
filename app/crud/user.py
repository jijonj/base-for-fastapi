# crud/user.py
from sqlalchemy.orm import Session
from app.models.user import User  # Direct import of User model
from app.schemas.user import UserCreate  # Assuming UserCreate is in app/schemas/user.py

def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(email=user.email, username=user.username, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.user import User, UserCreate  # Adjusted import statement
from ..crud.user import create_user  # Adjusted import statement
from ..dependencies import get_db
from ..models.user import User as UserModel

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@router.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(UserModel).all()
from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        from_attributes = True
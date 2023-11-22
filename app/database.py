from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL, for example, a SQLite URL for local development
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Replace with your database URL

# Create the SQLAlchemy engine
# If using SQLite, connect_args={"check_same_thread": False} is needed for time-based access control
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Each instance of the SessionLocal class will be a database session
# The class itself is not a database session yet
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# We will inherit from this class to create each of the database models or classes
Base = declarative_base()

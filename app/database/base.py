from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import Settings

# Replace the following with your actual PostgreSQL connection information
# Format: postgresql://username:password@host:port/dbname
DATABASE_URL = f"postgresql://{Settings.db_username}:{Settings.db_password}@{Settings.db_host}:{Settings.db_port}/{Settings.db_name}"

# Create a SQLAlchemy database engine
engine = create_engine(DATABASE_URL)

# Create a session factory for creating database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()

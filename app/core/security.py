from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from passlib.context import CryptContext
from core.config import Settings

# Initialize a CryptContext for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
settings = Settings()

def verify_password(plain_password, hashed_password):
    """Verify a plain text password against its hashed version."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """Hash a plain text password."""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt

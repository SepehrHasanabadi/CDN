from jose import jwt
from passlib.context import CryptContext
from app.core.config import Settings

# Initialize a CryptContext for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
settings = Settings()


def verify_password(plain_password, hashed_password):
    """Verify a plain text password against its hashed version."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """Hash a plain text password."""
    return pwd_context.hash(password)


def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(
        to_encode, settings.secret_key, algorithm=settings.algorithm
    )
    return encoded_jwt

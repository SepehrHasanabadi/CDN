from fastapi import HTTPException, Header, status
from jose import JWTError, jwt
from app.core.config import Settings

settings = Settings()


def verify_token(token: str = Header(...)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token, settings.secret_key, algorithms=[settings.algorithm]
        )
        return payload["sub"]
    except JWTError:
        raise credentials_exception

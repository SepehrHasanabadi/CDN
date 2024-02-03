from fastapi import Header
from jose import JWTError, jwt
from app.core.config import Settings
from app.utils.exceptions import credentials_exception

settings = Settings()


def verify_token(token: str = Header(...)):
    try:
        payload = jwt.decode(
            token, settings.secret_key, algorithms=[settings.algorithm]
        )
        return payload["sub"]
    except JWTError:
        raise credentials_exception

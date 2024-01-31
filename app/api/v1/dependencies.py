from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from core.config import Settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_token_header(token: str = Depends(oauth2_scheme)):
    return token


def verify_token(token: str = Depends(get_token_header)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token, Settings.secret_key, algorithms=[Settings.algorithm]
        )
        return payload
    except JWTError:
        raise credentials_exception

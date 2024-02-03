from fastapi import HTTPException
from starlette import status


credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

already_exists_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Resource already exists",
    headers={"WWW-Authenticate": "Bearer"},
)
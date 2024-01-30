from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..crud.user import create_user_in_db, get_user_by_username
from app.api.v1.models.user import UserCreate, UserCredential
from app.core.security import create_access_token, get_password_hash, verify_password
from app.database.session import get_db

router = APIRouter()


@router.post("/users/")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if the username already exists in the database
    # Perform necessary validation logic (e.g., password complexity requirements)

    # Hash the password before storing it in the database
    hashed_password = get_password_hash(user.password)
    db_user = create_user_in_db(db, user.username, hashed_password)

    return {"username": db_user.username}


@router.post("/token/")
async def token(user: UserCredential, db: Session = Depends(get_db)):
    # Check if the username already exists in the database
    # Perform necessary validation logic (e.g., password complexity requirements)

    # Hash the password before storing it in the database
    db_user = get_user_by_username(db, user.username)
    verified = verify_password(db_user.password, user.password)
    if not verified:
        return None
    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

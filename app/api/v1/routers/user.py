from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..crud.user import create_user_in_db, get_user_by_username
from ..schemas.user import UserCreate, UserCredential
from app.core.security import create_access_token, get_password_hash, verify_password
from app.database.session import get_db
from app.utils.exceptions import credentials_exception, already_exists_exception

router = APIRouter()


@router.post("/signup/")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user.password)
    db_user = create_user_in_db(db, user.username, hashed_password)
    if not db_user:
        raise already_exists_exception
    return {"username": db_user.username}


@router.post("/token/")
async def token(user: UserCredential, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    verified = verify_password(user.password, db_user.password)
    if not verified:
        raise credentials_exception
    access_token = create_access_token(data={"sub": db_user.username})
        
    return {"access_token": access_token, "token_type": "bearer"}

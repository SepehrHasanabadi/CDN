from sqlalchemy.orm import Session
from app.api.v1.models.user import User, UserCredential


def create_user_in_db(db: Session, username: str, password: str):
    existing_user = db.query(User).filter(User.username == username).first()
    if existing_user:
        return None
    db_user = User(username=username, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_username(db: Session, username: str):
    return db.query(UserCredential).filter(UserCredential.username == username).first()
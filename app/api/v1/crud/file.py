from sqlalchemy.orm import Session

from ..models.user import User

from ..models.file import File as CacheFile


def update_or_create_file_in_db(
    db: Session,
    memory_usage: float,
    minify_duration: float,
    path: str,
    size: str,
    type: str,
    user_id: int,
):
    existing_file = (
        db.query(CacheFile).filter(User.id == user_id, CacheFile.path == path).first()
    )
    fields = {
        "minify_ram_consumption": memory_usage,
        "minify_duration": minify_duration,
        "path": path,
        "size": size,
        "type": type,
        "user_id": user_id,
    }
    if not existing_file:
        db_user = CacheFile(**fields)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    else:
        for key, value in fields.items():
            setattr(existing_file, key, value)
        db.commit()
        return existing_file


def get_all_user_file(db: Session, username: str):
    return db.query(CacheFile).join(User).filter(User.username == username).all()

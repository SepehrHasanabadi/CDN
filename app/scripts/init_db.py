from app.database.base import Base, SessionLocal
from app.api.v1.models.user import User
from app.core.security import get_password_hash


def init():
    Base.metadata.create_all(bind=SessionLocal().bind)

    # Create a default user during initialization
    create_default_user()


def create_default_user():
    db = SessionLocal()

    # Check if the default user already exists
    existing_user = db.query(User).filter_by(username="parspack").first()
    if not existing_user:
        # Replace with your password hashing logic

        hashed_password = get_password_hash("Twu5hKXXKZEQaJ")

        # Create the default user
        default_user = User(username="parspack", password=hashed_password)
        db.add(default_user)
        db.commit()
        db.refresh(default_user)
        print("Default user created.")

    db.close()

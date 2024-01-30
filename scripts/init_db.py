from app.database.base import Base, SessionLocal
from app.api.v1.models.user import User


def init_db():
    # Create all tables defined in the models
    Base.metadata.create_all(bind=SessionLocal().bind)

    # Create a default user during initialization
    create_default_user()


def create_default_user():
    db = SessionLocal()

    # Check if the default user already exists
    existing_user = db.query(User).filter_by(username="admin").first()
    if not existing_user:
        # Replace with your password hashing logic
        hashed_password = "hashed_password"

        # Create the default user
        default_user = User(
            username="admin", email="admin@example.com", password=hashed_password
        )
        db.add(default_user)
        db.commit()
        db.refresh(default_user)
        print("Default user created.")

    db.close()


if __name__ == "__main__":
    init_db()

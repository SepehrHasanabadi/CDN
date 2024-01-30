from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI App"
    environment: str = "development"
    debug: bool = True
    secret_key: str = "your-secret-key"
    algorithm: str = "HS256"
    disabled_users: list = []

    class Config:
        env_file = ".env"

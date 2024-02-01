from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI App"
    environment: str = "development"
    debug: bool = True
    secret_key: str = "your-secret-key"
    algorithm: str = "HS256"
    disabled_users: list = []
    db_host: str = "localhost"
    db_username: str = "postgres"
    db_password: str = "password"
    db_port: str = 5432
    db_name: str = "postgres"
    upload_base_file: str = "/tmp/"

    class Config:
        env_file = "./app/.env"

import os

class Settings:
    PROJECT_NAME: str = "FastAPI Unpaid Work API"
    PROJECT_VERSION: str = "1.0.0"

    MYSQL_USER: str = os.getenv("MYSQL_USER", "fastapi_user")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD", "1234")
    MYSQL_SERVER: str = os.getenv("MYSQL_SERVER", "localhost")
    MYSQL_DB: str = os.getenv("MYSQL_DB", "mydatabase")

    DATABASE_URL: str = (
        f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}/{MYSQL_DB}"
    )

settings = Settings()

import os

HOST: str = os.getenv("HOST", "0.0.0.0")
PORT: int = int(os.getenv("PORT", "2000"))
DEBUG: bool = os.getenv("DEBUG", "False") == "True"

VERSION: str = os.getenv("VERSION", "1.0.0")
TITLE: str = os.getenv("TITLE", "MICROSERVICE-USER")

DATABASE_URL: str = os.getenv("DATABASE_URL", "")
DATABASE_URL_DEV: str = os.getenv("DATABASE_URL_DEV", "")

ALLOW_ORIGINS: list[str] = os.getenv("ALLOW_ORIGINS", "*").split(",")
ALLOW_CREDENTIALS: bool = os.getenv("ALLOW_CREDENTIALS", "False") == "True"
ALLOW_METHODS: list[str] = os.getenv("ALLOW_METHODS", "*").split(",")
ALLOW_HEADERS: list[str] = os.getenv("ALLOW_HEADERS", "*").split(",")
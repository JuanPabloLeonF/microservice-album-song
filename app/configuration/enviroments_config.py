"""
HOST: str = os.getenv("HOST", "0.0.0.0")
PORT: int = int(os.getenv("PORT", "2002"))
DEBUG: bool = os.getenv("DEBUG", "False") == "True"

VERSION: str = os.getenv("VERSION", "1.0.0")
TITLE: str = os.getenv("TITLE", "MICROSERVICE-ALBUM-SONG")

DATABASE_URL: str = os.getenv("DATABASE_URL", "")
DATABASE_URL_DEV: str = os.getenv("DATABASE_URL_DEV", "")

ALLOW_ORIGINS: list[str] = os.getenv("ALLOW_ORIGINS", "*").split(",")
ALLOW_CREDENTIALS: bool = os.getenv("ALLOW_CREDENTIALS", "False") == "True"
ALLOW_METHODS: list[str] = os.getenv("ALLOW_METHODS", "*").split(",")
ALLOW_HEADERS: list[str] = os.getenv("ALLOW_HEADERS", "*").split(",")

ALLOW_EXTENSIONS_FILE_IMG: list[str] = os.getenv("ALLOW_EXTENSIONS_FILE_IMG").split(",")
ALLOW_EXTENSIONS_FILE_MUSIC: list[str] = os.getenv("ALLOW_EXTENSIONS_FILE_MUSIC").split(",")
MAX_SIZE_IMG_FILE_MB: int = int(os.getenv("MAX_SIZE_IMG_FILE_MB"))
MAX_SIZE_MUSIC_FILE_MB: int = int(os.getenv("MAX_SIZE_MUSIC_FILE_MB"))
"""
from dotenv import dotenv_values

envConfig: dict = dotenv_values(".env")

HOST: str = envConfig.get("HOST", "0.0.0.0")
PORT: int = int(envConfig.get("PORT", "2002"))
DEBUG: bool = envConfig.get("DEBUG", "False") == "True"

VERSION: str = envConfig.get("VERSION", "1.0.0")
TITLE: str = envConfig.get("TITLE", "MICROSERVICE-ALBUM-SONG")

DATABASE_URL: str = envConfig.get("DATABASE_URL", "")
DATABASE_URL_DEV: str = envConfig.get("DATABASE_URL_DEV", "")

ALLOW_ORIGINS: list[str] = envConfig.get("ALLOW_ORIGINS", "*").split(",")
ALLOW_CREDENTIALS: bool = envConfig.get("ALLOW_CREDENTIALS", "False") == "True"
ALLOW_METHODS: list[str] = envConfig.get("ALLOW_METHODS", "*").split(",")
ALLOW_HEADERS: list[str] = envConfig.get("ALLOW_HEADERS", "*").split(",")

ALLOW_EXTENSIONS_FILE_IMG: list[str] = envConfig.get("ALLOW_EXTENSIONS_FILE_IMG").split(",")
ALLOW_EXTENSIONS_FILE_MUSIC: list[str] = envConfig.get("ALLOW_EXTENSIONS_FILE_MUSIC").split(",")
MAX_SIZE_IMG_FILE_MB: int = int(envConfig.get("MAX_SIZE_IMG_FILE_MB"))
MAX_SIZE_MUSIC_FILE_MB: int = int(envConfig.get("MAX_SIZE_MUSIC_FILE_MB"))
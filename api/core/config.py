import os
from dotenv import load_dotenv
from pydantic import BaseModel, BaseSettings

from api import __version__


load_dotenv()


class Settings(BaseSettings):
    STAGE: str = os.environ.get("STAGE")
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    VERSION: str = __version__


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "api"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        LOGGER_NAME: {"handlers": ["default"], "level": LOG_LEVEL},
    }


settings = Settings()
logs_config = LogConfig().dict()
app_config: dict[str, str] = {"title": "Fastapi Backend", "version": settings.VERSION}

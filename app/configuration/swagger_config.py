from fastapi import FastAPI
from app.configuration.enviroments_config import TITLE, VERSION

class ConfigurationSwagger:

    @staticmethod
    def configurationSwagger(app: FastAPI) -> None:
        app.title = TITLE
        app.version = VERSION
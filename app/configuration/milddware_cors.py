from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.configuration.enviroments_config import ALLOW_HEADERS, ALLOW_CREDENTIALS, ALLOW_METHODS, ALLOW_ORIGINS

class ConfigMiddleware:

    @staticmethod
    def configCors(app: FastAPI) -> None:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=ALLOW_ORIGINS,
            allow_credentials=ALLOW_CREDENTIALS,
            allow_methods=ALLOW_METHODS,
            allow_headers=ALLOW_HEADERS,
        )

from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.configuration.exceptions_personalities import ErrorSessionDatabase
from app.src.infrastructure.outputs.mysql.settings.database_config import DatabaseConfiguration

class AsyncContextManagerConfig:

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        try:
            await DatabaseConfiguration.runDatabase()
            yield
        except Exception as error:
            raise ErrorSessionDatabase(error)
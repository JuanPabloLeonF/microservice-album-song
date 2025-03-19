import os
from fastapi import FastAPI
from app.configuration.enviroments_config import HOST, PORT, DEBUG
from app.configuration.milddware_cors import ConfigMiddleware
from app.configuration.swagger_config import ConfigurationSwagger
from app.configuration.routers_config import ConfigurationRouter
from app.configuration.exceptions_handlers_global import ErrorsHandlersGlobals
from app.configuration.async_context_manager import AsyncContextManagerConfig

app: FastAPI = FastAPI(
    debug=DEBUG,
    lifespan=AsyncContextManagerConfig.lifespan,
    exception_handlers=ErrorsHandlersGlobals.registerHandlersMethodsDict(),
    routes=ConfigurationRouter.registerRouters(),
)

ConfigurationSwagger.configurationSwagger(app=app)
ConfigMiddleware.configCors(app=app)

if __name__ == "__main__":
    os.system(f"uvicorn main:app --host {HOST} --port {PORT} --reload")
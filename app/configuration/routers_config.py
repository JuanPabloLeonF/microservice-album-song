from starlette.routing import BaseRoute

from app.src.infrastructure.inputs.rest.controllers.controller_user import routerUser

class ConfigurationRouter:

    @staticmethod
    def registerRouters() -> list[BaseRoute]:
        return list(routerUser.routes)
from starlette.routing import BaseRoute

from app.src.infrastructure.inputs.rest.controllers.song_controller import songRouter

class ConfigurationRouter:

    @staticmethod
    def registerRouters() -> list[BaseRoute]:
        return list(songRouter.routes)
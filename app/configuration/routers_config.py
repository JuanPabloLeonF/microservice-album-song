from starlette.routing import BaseRoute
from app.src.infrastructure.inputs.rest.controllers.song_controller import songRouter
from app.src.infrastructure.inputs.rest.controllers.album_controller import albumRouter

class ConfigurationRouter:

    @staticmethod
    def registerRouters() -> list[BaseRoute]:
        return list(songRouter.routes) + list(albumRouter.routes)
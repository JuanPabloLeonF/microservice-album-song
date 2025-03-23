from abc import ABC, abstractmethod

from app.src.application.dto.response_album import AlbumResponse
from app.src.application.dto.request_album import AlbumRequest

class IAlbumHandler(ABC):

    @abstractmethod
    async def getAll(self, page: int, limit: int) -> list[AlbumResponse]:
        pass

    @abstractmethod
    async def getById(self, id: str) -> AlbumResponse:
        pass

    @abstractmethod
    async def getByAuthor(self, author: str, page: int, limit: int) -> list[AlbumResponse]:
        pass

    @abstractmethod
    async def create(self, request: AlbumRequest) -> AlbumResponse:
        pass

    @abstractmethod
    async def updateById(self, id: str, request: AlbumRequest) -> AlbumResponse:
        pass

    @abstractmethod
    async def deleteById(self, id: str) -> str:
        pass
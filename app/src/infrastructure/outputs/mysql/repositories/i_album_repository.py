from abc import ABC, abstractmethod
from app.src.infrastructure.outputs.mysql.entities.album_entity import AlbumEntity

class IAlbumRepository(ABC):

    @abstractmethod
    async def getAll(self, page: int, limit: int) -> list[AlbumEntity]:
        pass

    @abstractmethod
    async def getById(self, id: str) -> AlbumEntity:
        pass

    @abstractmethod
    async def getByAuthor(self, author: str, page: int, limit: int) -> list[AlbumEntity]:
        pass

    @abstractmethod
    async def create(self, albumEntity: AlbumEntity) -> AlbumEntity:
        pass

    @abstractmethod
    async def updateById(self, id: str, albumUpdate: AlbumEntity) -> AlbumEntity:
        pass

    @abstractmethod
    async def deleteById(self, id: str) -> str:
        pass
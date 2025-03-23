from abc import ABC, abstractmethod
from app.src.domain.models.album_model import AlbumModel

class IAlbumService(ABC):

    @abstractmethod
    async def getAll(self, page: int, limit: int) -> list[AlbumModel]:
        pass

    @abstractmethod
    async def getById(self, id: str) -> AlbumModel:
        pass

    @abstractmethod
    async def getByAuthor(self, author: str, page: int, limit: int) -> list[AlbumModel]:
        pass

    @abstractmethod
    async def create(self, albumModel: AlbumModel) -> AlbumModel:
        pass

    @abstractmethod
    async def updateById(self, id: str, albumUpdate: AlbumModel) -> AlbumModel:
        pass

    @abstractmethod
    async def deleteById(self, id: str) -> str:
        pass
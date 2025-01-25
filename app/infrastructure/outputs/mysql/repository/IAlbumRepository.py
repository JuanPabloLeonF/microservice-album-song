from abc import ABC, abstractmethod

from app.infrastructure.outputs.mysql.entities.AlbumEntity import AlbumEntity

class IAlbumRepository(ABC):

    @abstractmethod
    def getALl(self) -> list[AlbumEntity]:
        pass

    @abstractmethod
    def create(self, album: AlbumEntity) -> AlbumEntity:
        pass

    @abstractmethod
    def getById(self, id: str) -> AlbumEntity:
        pass

    @abstractmethod
    def updateSingleDataById(self, id: str, album: AlbumEntity) -> AlbumEntity:
        pass

    @abstractmethod
    def deleteById(self, id: str) -> str:
        pass

    @abstractmethod
    def updateImgUrlSingleDataById(self, id: str, imageUrl: str) -> AlbumEntity:
        pass

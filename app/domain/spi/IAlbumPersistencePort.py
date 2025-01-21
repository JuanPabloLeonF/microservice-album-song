from abc import ABC, abstractmethod
from app.domain.models.AlbumModel import AlbumModel

class IAlbumPersistencePort(ABC):

    @abstractmethod
    def getAll(self) -> list[AlbumModel]:
        pass

    @abstractmethod
    def create(self, album: AlbumModel) -> AlbumModel:
        pass

    @abstractmethod
    def getById(self, id: str) -> AlbumModel:
        pass

    @abstractmethod
    def updateSingleDataById(self, id: str, album: AlbumModel) -> AlbumModel:
        pass

    @abstractmethod
    def deleteById(self, id: str) -> str:
        pass

    @abstractmethod
    def updateImgUrlSingleDataById(self, id: str, imageUrl: str) -> AlbumModel:
        pass
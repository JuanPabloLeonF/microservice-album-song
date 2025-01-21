from abc import ABC, abstractmethod
from flask import Request
from app.domain.models.AlbumModel import AlbumModel

class IAlbumServicePort(ABC):

    @abstractmethod
    def getAll(self) -> list[AlbumModel]:
        pass

    @abstractmethod
    def create(self, album: AlbumModel, request: Request) -> AlbumModel:
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
    def updateImgUrlSingleDataById(self, id: str, request: Request) -> AlbumModel:
        pass


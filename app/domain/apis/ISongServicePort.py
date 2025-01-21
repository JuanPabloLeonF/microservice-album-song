from abc import ABC, abstractmethod
from app.domain.models.SongModel import SongModel
from flask import Request

class ISongServicePort(ABC):

    @abstractmethod
    def getAll(self) -> list[SongModel]:
        pass

    @abstractmethod
    def createWithReferenceToAlbum(self, songModel: SongModel, request: Request) -> SongModel:
        pass

    @abstractmethod
    def getById(self, id: str) -> SongModel:
        pass

    @abstractmethod
    def updateByIdWithReferenceToAlbum(self, id: str, songModel: SongModel) -> SongModel:
        pass

    @abstractmethod
    def deleteById(self, id: str) -> str:
        pass

    @abstractmethod
    def getSongsByGender(self, gender: str) -> list[SongModel]:
        pass

    @abstractmethod
    def updateImgUrlById(self, id: str, request: Request) -> SongModel:
        pass
from abc import ABC, abstractmethod
from app.domain.models.SongModel import SongModel

class ISongPersistencePort(ABC):

    @abstractmethod
    def getAll(self) -> list[SongModel]:
        pass

    @abstractmethod
    def createWithReferenceToAlbum(self, song: SongModel) -> SongModel:
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
    def updateImgUrlById(self, id: str, imageUrl: str) -> SongModel:
        pass
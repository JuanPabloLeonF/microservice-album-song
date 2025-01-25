from abc import ABC, abstractmethod
from app.infrastructure.outputs.mysql.entities.SongEntity import SongEntity
from app.domain.models.SongModel import SongModel

class ISongRepository(ABC):

    @abstractmethod
    def getAll(self) -> list[SongEntity]:
        pass

    @abstractmethod
    def createWithReferenceToAlbum(self, song: SongModel) -> SongEntity:
        pass

    @abstractmethod
    def getById(self, id: str) -> SongEntity:
        pass

    @abstractmethod
    def updateByIdWithReferenceToAlbum(self, id: str, songEntity: SongEntity) -> SongEntity:
        pass

    @abstractmethod
    def deleteById(self, id: str) -> str:
        pass

    @abstractmethod
    def getSongsByGender(self, gender: str) -> list[SongEntity]:
        pass

    @abstractmethod
    def updateImgUrlById(self, id: str, imageUrl: str) -> SongEntity:
        pass
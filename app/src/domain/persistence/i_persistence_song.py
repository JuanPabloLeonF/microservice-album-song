from abc import ABC, abstractmethod
from app.src.domain.models.song_model import SongModel

class ISongPersistence(ABC):

    @abstractmethod
    async def getAll(self, page: int, limit: int) -> list[SongModel]:
        pass

    @abstractmethod
    async def getById(self, id: str) -> SongModel:
        pass

    @abstractmethod
    async def getByGender(self, gender: str, page: int, limit: int) -> list[SongModel]:
        pass

    @abstractmethod
    async def create(self, song: SongModel) -> SongModel:
        pass

    @abstractmethod
    async def updateById(self, song: SongModel, id: str) -> SongModel:
        pass

    @abstractmethod
    async def deleteById(self, id: str) -> str:
        pass
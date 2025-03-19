from abc import ABC, abstractmethod
from app.src.infrastructure.outputs.mysql.entities.song_entity import SongEntity

class ISongRepository(ABC):

    @abstractmethod
    async def getAll(self, page: int, limit: int) -> list[SongEntity]:
        pass

    @abstractmethod
    async def getById(self, id: str) -> SongEntity:
        pass

    @abstractmethod
    async def getByGender(self, gender: str, page: int, limit: int) -> list[SongEntity]:
        pass

    @abstractmethod
    async def create(self, song: SongEntity) -> SongEntity:
        pass

    @abstractmethod
    async def updateById(self, song: SongEntity, id: str) -> SongEntity:
        pass

    @abstractmethod
    async def deleteById(self, id: str) -> str:
        pass
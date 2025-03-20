from abc import ABC, abstractmethod

from app.src.application.dto.request_song import RequestSong
from app.src.application.dto.response_song import ResponseSong

class ISongHandler(ABC):

    @abstractmethod
    async def getAll(self, page: int, limit: int) -> list[ResponseSong]:
        pass

    @abstractmethod
    async def getById(self, id: str) -> ResponseSong:
        pass

    @abstractmethod
    async def getByGender(self, gender: str, page: int, limit: int) -> list[ResponseSong]:
        pass

    @abstractmethod
    async def create(self, request: RequestSong) -> ResponseSong:
        pass

    @abstractmethod
    async def updateById(self, request: RequestSong, id: str) -> ResponseSong:
        pass

    @abstractmethod
    async def deleteById(self, id: str) -> str:
        pass
from abc import ABC, abstractmethod
from flask import Response, Request

class IAlbumHandler(ABC):

    @abstractmethod
    def getAll(self) -> tuple[Response, int]:
        pass

    @abstractmethod
    def create(self, request: Request) -> tuple[Response, int]:
        pass

    @abstractmethod
    def getById(self, id: str) -> tuple[Response, int]:
        pass

    @abstractmethod
    def updateSingleDataById(self, id: str, request: dict) -> tuple[Response, int]:
        pass

    @abstractmethod
    def deleteById(self, id: str) -> tuple[Response, int]:
        pass

    @abstractmethod
    def updateImgUrlSingleDataById(self, id: str, request: Request) -> tuple[Response, int]:
        pass
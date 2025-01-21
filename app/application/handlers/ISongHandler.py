from abc import ABC, abstractmethod
from flask import Response, Request

class ISongHandler(ABC):

    @abstractmethod
    def getAll(self) -> tuple[Response, int]:
        pass

    @abstractmethod
    def createWithReferenceToAlbum(self, request: Request) -> tuple[Response, int]:
        pass

    @abstractmethod
    def getById(self, id: str) -> tuple[Response, int]:
        pass

    @abstractmethod
    def updateByIdWithReferenceToAlbum(self, id: str, request: dict) -> tuple[Response, int]:
        pass

    @abstractmethod
    def deleteById(self, id: str) -> tuple[Response, int]:
        pass

    @abstractmethod
    def getSongsByGender(self, gender: str) -> tuple[Response, int]:
        pass

    @abstractmethod
    def updateImgUrlById(self, id: str, request: Request) -> tuple[Response, int]:
        pass
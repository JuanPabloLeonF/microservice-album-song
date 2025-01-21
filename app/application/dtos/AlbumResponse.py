from app.application.dtos.SongResponse import SongResponse


class AlbumResponse:

    def __init__(self, id: str, name: str, author: str, dateCreation: str, description: str, imageUrl: str, songs: list[SongResponse]):
        self.__id: str = id
        self.__name: str = name
        self.__author: str = author
        self.__dateCreation: str = dateCreation
        self.__description: str = description
        self.__imageUrl: str = imageUrl
        self.__songs: list[SongResponse] = songs

    def getId(self) -> str:
        return self.__id

    def getName(self) -> str:
        return self.__name

    def getAuthor(self) -> str:
        return self.__author

    def getDateCreation(self) -> str:
        return self.__dateCreation

    def getDescription(self) -> str:
        return self.__description

    def getImageUrl(self) -> str:
        return self.__imageUrl

    def getSongs(self) -> list[SongResponse]:
        return self.__songs

    def setName(self, name: str):
        self.__name = name

    def setAuthor(self, author: str):
        self.__author = author

    def setDateCreation(self, dateCreation: str):
        self.__dateCreation = dateCreation

    def setDescription(self, description: str):
        self.__description = description

    def setImageUrl(self, imageUrl: str):
        self.__imageUrl = imageUrl

    def setSongs(self, songs: list[dict]):
        self.__songs = songs

    def __str__(self):
        return f"Id: {self.__id}, Name: {self.__name}, Author: {self.__author}, DateCreation: {self.__dateCreation}, Description: {self.__description}, ImageUrl: {self.__imageUrl}, Songs: {self.__songs}"

    def getJSON(self) -> dict:
        return {
            "id": self.__id,
            "name": self.__name,
            "author": self.__author,
            "dateCreation": self.__dateCreation,
            "description": self.__description,
            "imageUrl": self.__imageUrl,
            "songs": [ song.getJSON() for song in self.__songs]
        }
from app.src.domain.models.song_model import SongModel

class AlbumModel:

    def __init__(self, id: str, name: str, author: str, dateCreation: str, description: str, imageCoverUrl: str, songs: list[SongModel]):
        self.__id: str = id
        self.__name: str = name
        self.__author: str = author
        self.__dateCreation: str = dateCreation
        self.__description: str = description
        self.__imageCoverUrl: str = imageCoverUrl
        self.__songs: list[SongModel] = songs

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

    def getImageCoverUrl(self) -> str:
        return self.__imageCoverUrl

    def getSongs(self) -> list[SongModel]:
        return self.__songs

    def setName(self, name: str):
        self.__name = name

    def setAuthor(self, author: str):
        self.__author = author

    def setDateCreation(self, dateCreation: str):
        self.__dateCreation = dateCreation

    def setDescription(self, description: str):
        self.__description = description

    def setImageCoverUrl(self, imageUrl: str):
        self.__imageCoverUrl = imageUrl

    def setSongs(self, songs: list[SongModel]):
        self.__songs = songs

    def __str__(self):
        return f"Id: {self.__id}, Name: {self.__name}, Author: {self.__author}, DateCreation: {self.__dateCreation}, Description: {self.__description}, ImageUrl: {self.__imageCoverUrl}, Songs: {self.__songs}"

    def getJSON(self):
        return {
            "id": self.__id,
            "name": self.__name,
            "author": self.__author,
            "dateCreation": self.__dateCreation,
            "description": self.__description,
            "imageCoverUrl": self.__imageCoverUrl,
            "songs": self.__songs
        }
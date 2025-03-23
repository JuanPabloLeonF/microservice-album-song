from fastapi import UploadFile

class AlbumRequest:

    def __init__(self, name: str, author: str, dateCreation: str, description: str, imageFile: UploadFile):
        self.__name: str = name
        self.__author: str = author
        self.__dateCreation: str = dateCreation
        self.__description: str = description
        self.__imageFile: UploadFile = imageFile

    def getName(self) -> str:
        return self.__name

    def getAuthor(self) -> str:
        return self.__author

    def getDateCreation(self) -> str:
        return self.__dateCreation

    def getDescription(self) -> str:
        return self.__description

    def getImageFile(self) -> UploadFile:
        return self.__imageFile

    def setName(self, name: str):
        self.__name = name

    def setAuthor(self, author: str):
        self.__author = author

    def setDateCreation(self, dateCreation: str):
        self.__dateCreation = dateCreation

    def setDescription(self, description: str):
        self.__description = description

    def setImageFile(self, imageFile: UploadFile):
        self.__imageFile = imageFile


    def getJSON(self):
        return {
            "name": self.__name,
            "author": self.__author,
            "dateCreation": self.__dateCreation,
            "description": self.__description,
            "imageFile": self.__imageFile
        }
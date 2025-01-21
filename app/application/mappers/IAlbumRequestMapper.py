from flask import Request
from app.domain.models.AlbumModel import AlbumModel
from app.domain.models.SongModel import SongModel


class IAlbumRequestMapper:

    @staticmethod
    def mapperRequestDataToAlbumModel(request: Request) -> AlbumModel:
        return AlbumModel(
            id="123",
            name=request.form.get("name"),
            author=request.form.get("author"),
            dateCreation=request.form.get("dateCreation"),
            description=request.form.get("description"),
            imageUrl="",
            songs=[]
        )

    @staticmethod
    def mapperAlbumModelToAlbumModelUpdate(request: dict) -> AlbumModel:
        return AlbumModel(
            id="",
            name=request.get("name"),
            author=request.get("author"),
            dateCreation=request.get("dateCreation"),
            description=request.get("description"),
            imageUrl="",
            songs=[]
        )
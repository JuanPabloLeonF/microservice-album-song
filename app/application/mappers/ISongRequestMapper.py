from app.domain.models.SongModel import SongModel
from flask import Request
import json


class ISongRequestMapper:

    @staticmethod
    def mapperRequestDataToSongModel(request: Request) -> SongModel:

        return SongModel(
            id="123",
            name=request.form.get('name'),
            singer=request.form.get('singer'),
            duration=int(request.form.get('duration')),
            gender=json.loads(request.form.get('gender')),
            imgUrl="",
            albumId=request.form.get("albumId")
        )

    @staticmethod
    def mapperRequestDataToSongModelUpdate(request: dict) -> SongModel:
        return SongModel(
            id="",
            name=request.get("name"),
            singer=request.get("singer"),
            duration=request.get("duration"),
            gender=request.get("gender"),
            albumId=request.get("albumId"),
            imgUrl=""
        )
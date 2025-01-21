from enum import unique

from app.infrastructure.outputs.sqlites.configurations.DatabaseConfiguration import db
from sqlalchemy import JSON
import uuid

class SongEntity(db.Model):
    __tablename__  = 'songs'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable=False)
    singer = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    gender = db.Column(JSON, nullable=False)
    imgUrl = db.Column(db.String(255), unique=False, nullable=False)
    albumId = db.Column(db.String(36), db.ForeignKey('albums.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, name: str, singer: str, duration: int, gender: list[str], albumId: str, imgUrl: str):
        self.name = name
        self.singer = singer
        self.duration = duration
        self.gender = gender
        self.albumId = albumId
        self.imgUrl = imgUrl

    def getId(self) -> str:
        return self.id

    def getName(self) -> str:
        return self.name

    def getSinger(self) -> str:
        return self.singer

    def getDuration(self) -> int:
        return self.duration

    def getGender(self) -> list[str]:
        return self.gender

    def getAlbumId(self) -> str:
        return self.albumId

    def getImgUrl(self) -> str:
        return self.imgUrl

    def getJSON(self):
        return {
            "id": self.id,
            "name": self.name,
            "singer": self.singer,
            "duration": self.duration,
            "gender": self.gender,
            "imgUrl": self.imgUrl,
            "albumId": self.albumId
        }
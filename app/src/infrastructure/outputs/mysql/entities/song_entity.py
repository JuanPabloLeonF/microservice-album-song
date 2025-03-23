import uuid
from sqlalchemy import JSON,Column, Integer, String, ForeignKey
from app.src.infrastructure.outputs.mysql.settings.database_config import DatabaseConfiguration

class SongEntity(DatabaseConfiguration.BaseModels):

    __tablename__  = 'song'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255), nullable=False)
    singer = Column(String(255), nullable=False)
    duration = Column(Integer, nullable=False)
    gender = Column(JSON, nullable=False)
    imgCoverUrl = Column(String(100), unique=True, nullable=False)
    musicUrl = Column(String(100), unique=True, nullable=False)
    albumId = Column(String(36), ForeignKey('album.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, name: str, singer: str, duration: int, gender: list[str], albumId: str, imgCoverUrl: str, musicUrl: str):
        self.name = name
        self.singer = singer
        self.duration = duration
        self.gender = gender
        self.albumId = albumId
        self.imgCoverUrl = imgCoverUrl
        self.musicUrl = musicUrl

    def getId(self) -> str:
        return self.id

    def getName(self) -> str:
        return self.name

    def getMusicUrl(self) -> str:
        return self.musicUrl

    def getSinger(self) -> str:
        return self.singer

    def getDuration(self) -> int:
        return self.duration

    def getGender(self) -> list[str]:
        return self.gender

    def getAlbumId(self) -> str:
        return self.albumId

    def getImgCoverUrl(self) -> str:
        return self.imgCoverUrl

    def getJSON(self):
        return {
            "id": self.id,
            "name": self.name,
            "singer": self.singer,
            "duration": self.duration,
            "gender": self.gender,
            "imgCoverUrl": self.imgCoverUrl,
            "albumId": self.albumId,
            "musicFile": self.musicUrl
        }
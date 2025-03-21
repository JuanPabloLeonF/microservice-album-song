import uuid
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.src.infrastructure.outputs.mysql.settings.database_config import DatabaseConfiguration
from app.src.infrastructure.outputs.mysql.entities.song_entity import SongEntity

class AlbumEntity(DatabaseConfiguration.BaseModels):
    __tablename__ = 'album'

    id = Column(String(20), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    dateCreation = Column(String(36), nullable=False)
    description = Column(String(255), nullable=False)
    imageCoverUrl = Column(String(255), nullable=False)
    songs = relationship(
        argument='SongEntity',
        backref='album',
        lazy=True,
        cascade="all, delete",
        uselist=True
    )

    def __init__(self, name: str, author: str, dateCreation: str, description: str, imageCoverUrl: str, songs: list[SongEntity]):
        self.name = name
        self.author = author
        self.dateCreation = dateCreation
        self.description = description
        self.imageCoverUrl = imageCoverUrl
        self.songs = songs

    def getId(self) -> str:
        return self.id

    def getName(self) -> str:
        return self.name

    def getAuthor(self) -> str:
        return self.author

    def getDateCreation(self) -> str:
        return self.dateCreation

    def getDescription(self) -> str:
        return self.description

    def getImageCoverUrl(self) -> str:
        return self.imageCoverUrl

    def getSongs(self) -> list[SongEntity]:
        return self.songs

    def getJSON(self):
        return {
            "id": self.id,
            "name": self.name,
            "author": self.author,
            "dateCreation": self.dateCreation,
            "description": self.description,
            "imageCoverUrl": self.imageCoverUrl,
            "songs": self.songs
        }
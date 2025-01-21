from app.infrastructure.outputs.sqlites.configurations.DatabaseConfiguration import db
import uuid
from app.infrastructure.outputs.sqlites.entities.SongEntity import SongEntity


class AlbumEntity(db.Model):
    __tablename__ = 'albums'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    dateCreation = db.Column(db.String(36), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    imageUrl = db.Column(db.String(255), nullable=False)
    songs = db.relationship('SongEntity', backref='album', lazy=True, cascade="all, delete")

    def __init__(self , name: str, author: str, dateCreation: str, description: str, imageUrl: str, songs: list[SongEntity]):
        self.name = name
        self.author = author
        self.dateCreation = dateCreation
        self.description = description
        self.imageUrl = imageUrl
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

    def getImageUrl(self) -> str:
        return self.imageUrl

    def getSongs(self) -> list[SongEntity]:
        return self.songs

    def getJSON(self):
        return {
            "id": self.id,
            "name": self.name,
            "author": self.author,
            "dateCreation": self.dateCreation,
            "description": self.description,
            "imageUrl": self.imageUrl,
            "songs": self.songs
        }
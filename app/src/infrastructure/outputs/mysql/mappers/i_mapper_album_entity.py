from app.src.domain.models.album_model import AlbumModel
from app.src.domain.models.song_model import SongModel
from app.src.infrastructure.outputs.mysql.entities.album_entity import AlbumEntity
from app.src.infrastructure.outputs.mysql.entities.song_entity import SongEntity
from app.src.infrastructure.outputs.mysql.mappers.i_mapper_song_entity import IMapperSongEntity

class IMapperAlbumEntity:

    @staticmethod
    def mapperAlbumEntityToAlbumModel(albumEntity: AlbumEntity) -> AlbumModel:
        listSongsModels: list[SongEntity] = []

        if len(albumEntity.getSongs()) > 0:
            listSongsModels: list[SongModel] = IMapperSongEntity.mapperListSongEntityToListSongModel(listSongEntity=albumEntity.songs)

        return AlbumModel(
            id=albumEntity.id,
            name=albumEntity.name,
            author=albumEntity.author,
            dateCreation=albumEntity.dateCreation,
            description=albumEntity.description,
            imageCoverUrl=albumEntity.imageCoverUrl,
            songs=listSongsModels
        )

    @staticmethod
    def mapperAlbumModelToAlbumEntity(albumModel: AlbumModel) -> AlbumEntity:
        listSongsEntity: list[SongEntity] = []

        if len(albumModel.getSongs()) > 0:
            listSongsEntity = IMapperSongEntity.mapperListSongModelToListSongEntity(listSongModel=albumModel.getSongs())

        return AlbumEntity(
            name=albumModel.getName(),
            author=albumModel.getAuthor(),
            dateCreation=albumModel.getDateCreation(),
            description=albumModel.getDescription(),
            imageCoverUrl=albumModel.getImageCoverUrl(),
            songs=listSongsEntity
        )

    @staticmethod
    def mapperListAlbumEntityToListAlbumModel(listAlbumEntity: list[AlbumEntity]) -> list[AlbumModel]:
        return [IMapperAlbumEntity.mapperAlbumEntityToAlbumModel(albumEntity=albumEntity) for albumEntity in listAlbumEntity]
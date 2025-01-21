from app.domain.models.AlbumModel import AlbumModel
from app.domain.models.SongModel import SongModel
from app.infrastructure.outputs.sqlites.entities.AlbumEntity import AlbumEntity
from app.infrastructure.outputs.sqlites.entities.SongEntity import SongEntity
from app.infrastructure.outputs.sqlites.mappers.ISongEntityMapper import ISongEntityMapper


class IAlbumEntityMapper:

    @staticmethod
    def mapperAlbumEntityToAlbumModel(albumEntity: AlbumEntity) -> AlbumModel:
        songsModels: list[SongModel] = list(
            map(
                lambda songEntity: ISongEntityMapper.mapperSongEntityToSongModel(songEntity),
                albumEntity.getSongs()
            )
        )

        return AlbumModel(
            id=albumEntity.getId(),
            name=albumEntity.getName(),
            author=albumEntity.getAuthor(),
            dateCreation=albumEntity.getDateCreation(),
            description=albumEntity.getDescription(),
            imageUrl=albumEntity.getImageUrl(),
            songs=songsModels
        )

    @staticmethod
    def mapperAlbumEntityListToAlbumModelList(albumEntityList: list[AlbumEntity]) -> list[AlbumModel]:
        return list(
            map(
                lambda albumEntity: IAlbumEntityMapper.mapperAlbumEntityToAlbumModel(albumEntity),
                albumEntityList
            )
        )

    @staticmethod
    def mapperAlbumModelToAlbumEntity(albumModel: AlbumModel) -> AlbumEntity:

        if not albumModel.getSongs():
            return AlbumEntity(
                name=albumModel.getName(),
                author=albumModel.getAuthor(),
                dateCreation=albumModel.getDateCreation(),
                description=albumModel.getDescription(),
                imageUrl=albumModel.getImageUrl(),
                songs= []
            )

        songsEntities: list[SongEntity] = list(
            map(
                lambda songModel: ISongEntityMapper.mapperSongModelToSongEntity(songModel),
                albumModel.getSongs()
            )
        )

        return AlbumEntity(
            name=albumModel.getName(),
            author=albumModel.getAuthor(),
            dateCreation=albumModel.getDateCreation(),
            description=albumModel.getDescription(),
            imageUrl=albumModel.getImageUrl(),
            songs= songsEntities
        )
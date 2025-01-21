from app.infrastructure.outputs.sqlites.entities.SongEntity import SongEntity
from app.domain.models.SongModel import SongModel

class ISongEntityMapper:

    @staticmethod
    def mapperSongEntityToSongModel(songEntity: SongEntity) -> SongModel:
        return SongModel(
            id = songEntity.getId(),
            name = songEntity.getName(),
            singer = songEntity.getSinger(),
            duration = songEntity.getDuration(),
            gender = songEntity.getGender(),
            imgUrl= songEntity.getImgUrl(),
            albumId = songEntity.getAlbumId()
        )

    @staticmethod
    def mapperSongEntityListToSongModelList(songEntityList: list[SongEntity]) -> list[SongModel]:
        return [ISongEntityMapper.mapperSongEntityToSongModel(songEntity) for songEntity in songEntityList]

    @staticmethod
    def mapperSongModelToSongEntity(songModel: SongModel) -> SongEntity:
        return SongEntity(
            name = songModel.getName(),
            singer = songModel.getSinger(),
            duration = songModel.getDuration(),
            gender = songModel.getGender(),
            imgUrl= songModel.getImgUrl(),
            albumId = songModel.getAlbumId()
        )
from app.src.domain.models.song_model import SongModel
from app.src.infrastructure.outputs.mysql.entities.song_entity import SongEntity

class IMapperSongEntity:

    @staticmethod
    def mapperSongEntityToSongModel(songEntity: SongEntity) -> SongModel:
        return SongModel(
            id=songEntity.getId(),
            name=songEntity.getName(),
            singer=songEntity.getSinger(),
            duration=songEntity.getDuration(),
            gender=songEntity.getGender(),
            albumId=songEntity.getAlbumId(),
            imgCoverUrl=songEntity.getImgCoverUrl(),
            musicUrl=songEntity.getMusicUrl()
        )

    @staticmethod
    def mapperSongModelToSongEntity(songModel: SongModel) -> SongEntity:
        return SongEntity(
            name=songModel.getName(),
            singer=songModel.getSinger(),
            duration=songModel.getDuration(),
            gender=songModel.getGender(),
            albumId=songModel.getAlbumId(),
            imgCoverUrl=songModel.getImgCoverUrl(),
            musicUrl=songModel.getMusicUrl()
        )

    @staticmethod
    def mapperListSongEntityToListSongModel(listSongEntity: list[SongEntity]) -> list[SongModel]:
        return [IMapperSongEntity.mapperSongEntityToSongModel(songEntity) for songEntity in listSongEntity]

    @staticmethod
    def mapperListSongModelToListSongEntity(listSongModel: list[SongModel]) -> list[SongEntity]:
        return [IMapperSongEntity.mapperSongModelToSongEntity(songModel) for songModel in listSongModel]
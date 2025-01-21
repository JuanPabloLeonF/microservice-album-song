from app.domain.models.SongModel import SongModel
from app.application.dtos.SongResponse import SongResponse


class ISongResponseMapper:

    @staticmethod
    def mapperSongModelToSongResponse(songModel: SongModel) -> SongResponse:

        return SongResponse(
            id=songModel.getId(),
            name=songModel.getName(),
            singer=songModel.getSinger(),
            duration=songModel.getDuration(),
            gender=songModel.getGender(),
            imgUrl=songModel.getImgUrl(),
            albumId=songModel.getAlbumId()
        )

    @staticmethod
    def mapperSongModelListToSongResponseList(songModelList: list[SongModel]) -> list[SongResponse]:

        if not isinstance(songModelList, list):
            raise TypeError("El argumento debe ser una instancia de list")

        return [ISongResponseMapper.mapperSongModelToSongResponse(songModel) for songModel in songModelList]
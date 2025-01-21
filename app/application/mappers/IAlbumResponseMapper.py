from app.application.dtos.AlbumResponse import AlbumResponse
from app.application.dtos.SongResponse import SongResponse
from app.application.mappers.ISongResponseMapper import ISongResponseMapper
from app.domain.models.AlbumModel import AlbumModel


class IAlbumResponseMapper:

    @staticmethod
    def mapperAlbumModelToAlbumResponse(albumModel: AlbumModel) -> AlbumResponse:
        songsResponse: list[SongResponse] = ISongResponseMapper.mapperSongModelListToSongResponseList(albumModel.getSongs())

        return AlbumResponse(
            id=albumModel.getId(),
            name=albumModel.getName(),
            author=albumModel.getAuthor(),
            dateCreation=albumModel.getDateCreation(),
            description=albumModel.getDescription(),
            imageUrl=albumModel.getImageUrl(),
            songs=songsResponse
        )

    @staticmethod
    def mapperAlbumModelListToAlbumResponseList(albumModelList: list[AlbumModel]) -> list[AlbumResponse]:
        return list(
            map(
                lambda album: IAlbumResponseMapper.mapperAlbumModelToAlbumResponse(album),
                albumModelList
            )
        )
from app.src.domain.models.album_model import AlbumModel
from app.src.application.dto.response_album import AlbumResponse
from app.src.application.dto.response_song import ResponseSong
from app.src.application.dto.request_album import AlbumRequest
from app.src.application.mappers.i_mapper_song_application import IMapperSongApplication
from app.src.application.utils.utils_file_application import UtilsFilesApplication

class IMapperAlbumApplication:

    @staticmethod
    def mapperResponseAlbumToResponseAlbumDict(albumResponse: AlbumResponse) -> AlbumResponse:
        listSongDict: list[ResponseSong] = [song.getJSON() for song in albumResponse.getSongs()]
        albumResponse.setSongs(listSongDict)
        return albumResponse.getJSON()

    @staticmethod
    def mapperListResponseAlbumToListResponseAlbumDict(listAlbumResponse: list[AlbumResponse]) -> list[AlbumResponse]:
        listSongDict: list[ResponseSong] = []
        for album in listAlbumResponse:
            for song in album.getSongs():
                listSongDict.append(song.getJSON())

        for album in listAlbumResponse:
            album.setSongs(listSongDict)

        return [album.getJSON() for album in listAlbumResponse]

    @staticmethod
    def mapperRequestAlbumToAlbumModel(request: AlbumRequest, imgUrlAlbum)-> AlbumModel:
        return AlbumModel(
            id="",
            author=request.getAuthor(),
            name=request.getName(),
            imageCoverUrl=imgUrlAlbum,
            description=request.getDescription(),
            dateCreation=request.getDateCreation(),
            songs=[]
        )

    @staticmethod
    def mapperAlbumModelToAlbumResponse(albumModel: AlbumModel) -> AlbumResponse:
        listSongResponse: list[ResponseSong] = IMapperSongApplication.mapperListSongModelToListResponseSong(
            listSongModel=albumModel.getSongs()
        )

        return AlbumResponse(
            id=albumModel.getId(),
            author=albumModel.getAuthor(),
            description=albumModel.getDescription(),
            name=albumModel.getName(),
            dateCreation=albumModel.getDateCreation(),
            imageCoverUrl=UtilsFilesApplication.convertFileToBase64(filePath=albumModel.getImageCoverUrl()),
            songs=listSongResponse
        )

    @staticmethod
    def mapperListAlbumModelToAlbumResponse(listAlbumModel: list[AlbumModel]) -> list[AlbumResponse]:
        return [IMapperAlbumApplication.mapperAlbumModelToAlbumResponse(albumModel=album) for album in listAlbumModel]
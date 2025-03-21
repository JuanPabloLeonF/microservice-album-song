from app.src.application.dto.request_song import RequestSong
from app.src.application.dto.response_song import ResponseSong
from app.src.domain.models.song_model import SongModel
from app.src.application.utils.utils_file_application import UtilsFilesApplication

class IMapperSongApplication:

    @staticmethod
    def mapperRequestSongToSongModel(requestSong: RequestSong, imgCoverUrl: str, musicUrl: str) -> SongModel:
        return SongModel(
            id="",
            name=requestSong.getName(),
            singer=requestSong.getSinger(),
            duration=requestSong.getDuration(),
            gender=requestSong.getGender(),
            albumId=requestSong.getAlbumId(),
            imgCoverUrl= imgCoverUrl,
            musicUrl= musicUrl
        )

    @staticmethod
    def mapperSongModelToResponseSong(songModel: SongModel) -> ResponseSong:
        return ResponseSong(
            id=songModel.getId(),
            name=songModel.getName(),
            singer=songModel.getSinger(),
            duration=songModel.getDuration(),
            gender=songModel.getGender(),
            imgCoverUrl=songModel.getImgCoverUrl(),
            albumId=UtilsFilesApplication.convertFileToBase64(filePath=songModel.getImgCoverUrl()),
            musicUrl=UtilsFilesApplication.convertFileToBase64(filePath=songModel.getMusicUrl())
        )

    @staticmethod
    def mapperListSongModelToListResponseSong(listSongModel: list[SongModel]) -> list[ResponseSong]:
        return [IMapperSongApplication.mapperSongModelToResponseSong(songModel) for songModel in listSongModel]
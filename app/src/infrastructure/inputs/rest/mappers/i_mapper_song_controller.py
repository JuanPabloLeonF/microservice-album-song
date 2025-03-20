from app.src.infrastructure.inputs.rest.dto.request_song_controller import SongRequestForm
from app.src.application.dto.request_song import RequestSong

class IMapperSongController:

    @staticmethod
    def mapperSongRequestFormToRequestSong(songRequestForm: SongRequestForm) -> RequestSong:
        return RequestSong(
            name=songRequestForm.name,
            singer=songRequestForm.singer,
            duration=songRequestForm.duration,
            gender=songRequestForm.gender,
            albumId=songRequestForm.albumId,
            imgCoverFile=songRequestForm.imgFile,
            musicFile=songRequestForm.musicFile
        )
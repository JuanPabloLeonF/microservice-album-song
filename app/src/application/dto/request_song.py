from fastapi import UploadFile

class RequestSong:
    def __init__(self, name: str, singer: str, duration: int, gender: list[str], albumId: str,
                 imgCoverFile: UploadFile, musicFile: UploadFile):
        self.name: str = name
        self.singer: str = singer
        self.duration: int = duration
        self.gender: list[str] = gender
        self.imgCoverFile: UploadFile = imgCoverFile
        self.albumId: str = albumId
        self.musicFile: UploadFile = musicFile

    def getMusicFile(self) -> UploadFile:
        return self.musicFile

    def getName(self) -> str:
        return self.name

    def getSinger(self) -> str:
        return self.singer

    def getDuration(self) -> int:
        return self.duration

    def getGender(self) -> list[str]:
        return self.gender

    def getImgCoverFile(self) -> UploadFile:
        return self.imgCoverFile

    def getAlbumId(self) -> str:
        return self.albumId

    def setName(self, name: str):
        self.name = name

    def setSinger(self, singer: str):
        self.singer = singer

    def setDuration(self, duration: int):
        self.duration = duration

    def setGender(self, gender: list[str]):
        self.gender = gender

    def setImgCoverFile(self, imgUrlFile: UploadFile):
        self.imgCoverFile = imgUrlFile

    def setAlbumId(self, albumId: str):
        self.albumId = albumId

    def setMusicFile(self, musicUrl: str):
        self.musicFile = musicUrl

    def getJSON(self):
        return {
            "name": self.name,
            "singer": self.singer,
            "duration": self.duration,
            "gender": self.gender,
            "imgCoverUrl": self.imgCoverFile,
            "albumId": self.albumId,
            "musicFile": self.musicFile
        }
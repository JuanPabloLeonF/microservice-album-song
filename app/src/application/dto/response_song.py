class ResponseSong:
    def __init__(self, id: str, name: str, singer: str, duration: int, gender: list[str], albumId: str, imgCoverUrl: str, musicUrl: str):
        self.id: str = id
        self.name: str = name
        self.singer: str = singer
        self.duration: int = duration
        self.gender: list[str] = gender
        self.imgCoverUrl: str = imgCoverUrl
        self.albumId: str = albumId
        self.musicUrl: str= musicUrl

    def getId(self) -> str:
        return self.id

    def getMusicUrl(self) -> str:
        return self.musicUrl

    def getName(self) -> str:
        return self.name

    def getSinger(self) -> str:
        return self.singer

    def getDuration(self) -> int:
        return self.duration

    def getGender(self) -> list[str]:
        return self.gender

    def getImgCoverUrl(self) -> str:
        return self.imgCoverUrl

    def getAlbumId(self) -> str:
        return self.albumId

    def setId(self, id: str):
        self.id = id

    def setName(self, name: str):
        self.name = name

    def setSinger(self, singer: str):
        self.singer = singer

    def setDuration(self, duration: int):
        self.duration = duration

    def setGender(self, gender: list[str]):
        self.gender = gender

    def setImgCoverUrl(self, imgUrl: str):
        self.imgCoverUrl = imgUrl

    def setAlbumId(self, albumId: str):
        self.albumId = albumId

    def setMusicUrl(self, musicUrl: str):
        self.musicUrl = musicUrl

    def getJSON(self):
        return {
            "id": self.id,
            "name": self.name,
            "singer": self.singer,
            "duration": self.duration,
            "gender": self.gender,
            "imgCoverUrl": self.imgCoverUrl,
            "albumId": self.albumId,
            "musicUrl": self.musicUrl
        }
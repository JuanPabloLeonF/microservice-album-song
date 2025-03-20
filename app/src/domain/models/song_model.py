class SongModel:
    def __init__(self, id: str, name: str, singer: str, duration: int, gender: list[str], albumId: str, imgCoverUrl: str, musicUrl: str):
        self.__id: str = id
        self.__name: str = name
        self.__singer: str = singer
        self.__duration: int = duration
        self.__gender: list[str] = gender
        self.__imgCoverUrl: str = imgCoverUrl
        self.__albumId: str = albumId
        self.musicUrl: str= musicUrl

    def getId(self) -> str:
        return self.__id

    def getMusicUrl(self) -> str:
        return self.musicUrl

    def getName(self) -> str:
        return self.__name

    def getSinger(self) -> str:
        return self.__singer

    def getDuration(self) -> int:
        return self.__duration

    def getGender(self) -> list[str]:
        return self.__gender

    def getImgCoverUrl(self) -> str:
        return self.__imgCoverUrl

    def getAlbumId(self) -> str:
        return self.__albumId

    def setId(self, id: str):
        self.__id = id

    def setName(self, name: str):
        self.__name = name

    def setSinger(self, singer: str):
        self.__singer = singer

    def setDuration(self, duration: int):
        self.__duration = duration

    def setGender(self, gender: list[str]):
        self.__gender = gender

    def setImgCoverUrl(self, imgUrl: str):
        self.__imgCoverUrl = imgUrl

    def setAlbumId(self, albumId: str):
        self.__albumId = albumId

    def setMusicUrl(self, musicUrl: str):
        self.musicUrl = musicUrl

    def getJSON(self):
        return {
            "id": self.__id,
            "name": self.__name,
            "singer": self.__singer,
            "duration": self.__duration,
            "gender": self.__gender,
            "imgCoverUrl": self.__imgCoverUrl,
            "albumId": self.__albumId,
            "musicFile": self.musicUrl
        }
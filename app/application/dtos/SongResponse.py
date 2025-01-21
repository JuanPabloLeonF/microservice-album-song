class SongResponse:
    def __init__(self, id: str, name: str, singer: str, duration: int, gender: list[str], albumId: str, imgUrl: str):
        self.__id: str = id
        self.__name: str = name
        self.__singer: str = singer
        self.__duration: int = duration
        self.__gender: list[str] = gender
        self.__imgUrl: str = imgUrl
        self.__albumId: str = albumId

    def getId(self) -> str:
        return self.__id

    def getName(self) -> str:
        return self.__name

    def getSinger(self) -> str:
        return self.__singer

    def getDuration(self) -> int:
        return self.__duration

    def getImgUrl(self) -> str:
        return self.__imgUrl

    def getGender(self) -> list[str]:
        return self.__gender

    def setId(self, id: str):
        self.__id = id

    def setName(self, name: str):
        self.__name = name

    def setSinger(self, singer: str):
        self.__singer = singer

    def setDuration(self, duration: int):
        self.__duration = duration

    def setImgUrl(self, imgUrl: str):
        self.__imgUrl = imgUrl

    def setGender(self, gender: list[str]):
        self.__gender = gender

    def __str__(self):
        return f"Id: {self.__id}, Name: {self.__name}, Singer: {self.__singer}, Duration: {self.__duration}, Gender: {self.__gender}, ImgUrl: {self.__imgUrl}, AlbumId: {self.__albumId}"

    def getJSON(self):
        return {
            "id": self.__id,
            "name": self.__name,
            "singer": self.__singer,
            "duration": self.__duration,
            "gender": self.__gender,
            "imgUrl": self.__imgUrl,
            "albumId": self.__albumId
        }
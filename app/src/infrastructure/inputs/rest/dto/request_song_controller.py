import json
from fastapi import Form, UploadFile, File

class SongRequestForm:
    def __init__(
        self,
        name: str = Form(min_length=3, max_length=200),
        singer: str = Form(min_length=5, max_length=200),
        duration: int = Form(min_length=1, max_length=10),
        gender: str = Form(),
        albumId: str = Form(),
        imgFile: UploadFile = File(),
        musicFile: UploadFile = File(),
    ):
        self.name = name
        self.singer = singer
        self.duration = duration
        self.gender = self.validateGender(value=gender)
        self.albumId = albumId
        self.imgFile = imgFile
        self.musicFile = musicFile

    @staticmethod
    def validateGender(value: str) -> list[str]:
        try:
            data: list[str] = json.loads(value)

            if not isinstance(data, list):
                raise ValueError("gender debe ser una lista de strings")

            if len(data) == 0:
                raise ValueError("gender debe tener al menos un elemento")

            for item in data:
                if not isinstance(item, str) or item.strip() == "":
                    raise ValueError("gender no puede estar vacio")

            return data
        except (ValueError, json.JSONDecodeError):
            raise ValueError("gender must be a list of strings")

    def getJSON(self) -> dict:
        return {
            "name": self.name,
            "singer": self.singer,
            "duration": self.duration,
            "gender": self.gender,
            "albumId": self.albumId,
            "imgFile": self.imgFile.filename,
            "musicFile": self.musicFile.filename
        }
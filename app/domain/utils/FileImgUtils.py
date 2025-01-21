from werkzeug.utils import secure_filename
import uuid
import os
import base64

from app.domain.validators.validatorsSongs import ValidatorsSongs
from app.domain.models.AlbumModel import AlbumModel
from app.domain.models.SongModel import SongModel


class FileImgUtils:

    @staticmethod
    def createDirectoryPublic(uploadFolder: str):
        os.makedirs(uploadFolder, exist_ok=True)

    @staticmethod
    def saveImgInDirectoryPublic(file, uploadFolder: str, folderName: str) -> str:
        if ValidatorsSongs.validateFileName(filename=file.filename):
            FileImgUtils.createDirectoryPublic(uploadFolder=uploadFolder)
            filename: str = secure_filename(str(uuid.uuid4()) + file.filename)
            filePath: str = os.path.join(uploadFolder, filename)
            file.save(filePath)
            if folderName is "albums":
                return f"albums/{filename}"
            return f"songs/{filename}"

    @staticmethod
    def deleteImgInDirectoryPublic(imageUrl: str):
        UPLOAD_FOLDER: str = os.path.join(os.getcwd(), 'public', imageUrl)
        if imageUrl.startswith("albums/"):
            os.remove(UPLOAD_FOLDER)
        else:
            os.remove(UPLOAD_FOLDER)

    @staticmethod
    def convertImgToBase64(imageUrl: str) -> str:
        UPLOAD_FOLDER: str = os.path.join(os.getcwd(), 'public', imageUrl)
        with open(UPLOAD_FOLDER, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")

    @staticmethod
    def convertListAlbumModelsWithImgBase64(listAlbumModel: list[AlbumModel]) -> list[AlbumModel]:

        listSongsModelsWithImgBase64: list[SongModel] = [
            FileImgUtils.convertSongModelWithImgBase64(songModel=songModel)
            for albumModel in listAlbumModel
            for songModel in albumModel.getSongs()
        ]

        return [
            AlbumModel(
                id=albumModel.getId(),
                name=albumModel.getName(),
                author=albumModel.getAuthor(),
                dateCreation=albumModel.getDateCreation(),
                description=albumModel.getDescription(),
                imageUrl= FileImgUtils.convertImgToBase64(imageUrl=albumModel.getImageUrl()),
                songs=listSongsModelsWithImgBase64
            ) for albumModel in listAlbumModel
        ]

    @staticmethod
    def convertAlbumModelWithImgBase64(albumModel: AlbumModel) -> AlbumModel:
        return AlbumModel(
            id=albumModel.getId(),
            name=albumModel.getName(),
            author=albumModel.getAuthor(),
            dateCreation=albumModel.getDateCreation(),
            description=albumModel.getDescription(),
            imageUrl= FileImgUtils.convertImgToBase64(imageUrl=albumModel.getImageUrl()),
            songs=albumModel.getSongs()
        )

    @staticmethod
    def convertListSongModelsWithImgBase64(listSongModel: list[SongModel]) -> list[SongModel]:
        return [
            SongModel(
                id=songModel.getId(),
                name=songModel.getName(),
                singer=songModel.getSinger(),
                gender=songModel.getGender(),
                duration=songModel.getDuration(),
                imgUrl= FileImgUtils.convertImgToBase64(imageUrl=songModel.getImgUrl()),
                albumId=songModel.getAlbumId()
            ) for songModel in listSongModel
        ]

    @staticmethod
    def convertSongModelWithImgBase64(songModel: SongModel) -> SongModel:
        return SongModel(
            id=songModel.getId(),
            name=songModel.getName(),
            singer=songModel.getSinger(),
            gender=songModel.getGender(),
            duration=songModel.getDuration(),
            imgUrl= FileImgUtils.convertImgToBase64(imageUrl=songModel.getImgUrl()),
            albumId=songModel.getAlbumId()
        )
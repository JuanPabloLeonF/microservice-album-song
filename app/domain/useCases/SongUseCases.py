from app.domain.apis.ISongServicePort import ISongServicePort
from app.domain.models.AlbumModel import AlbumModel
from app.domain.spi.IAlbumPersistencePort import IAlbumPersistencePort
from app.domain.spi.ISongPersistencePort import ISongPersistencePort
from app.domain.models.SongModel import SongModel
from app.domain.utils.FileImgUtils import FileImgUtils
from app.domain.validators.validatorsSongs import ValidatorsSongs
from flask import Request
import os

from app.infrastructure.exceptions.ExceptionHandlersGlobal import ValidateData


class SongUseCase(ISongServicePort):

    def __init__(self, iSongPersistencePort: ISongPersistencePort, iAlbumPersistencePort: IAlbumPersistencePort):
        self.iSongPersistencePort = iSongPersistencePort
        self.iAlbumPersistencePort = iAlbumPersistencePort

    def getAll(self) -> list[SongModel]:
        return FileImgUtils.convertListSongModelsWithImgBase64(listSongModel=self.iSongPersistencePort.getAll())

    def createWithReferenceToAlbum(self, songModel: SongModel, request: Request) -> SongModel:

        albumFound: AlbumModel = self.iAlbumPersistencePort.getById(id=songModel.getAlbumId())

        if not albumFound:
            raise ValidateData(f"El album con el id: {songModel.getAlbumId()} no existe")

        UPLOAD_FOLDER: str = os.path.join(os.getcwd(), 'public', 'songs')
        if ValidatorsSongs.validateRequestContainFile(request=request) and ValidatorsSongs.validateFields(songModel=songModel):
            file = request.files['file']
            imgUrl: str = FileImgUtils.saveImgInDirectoryPublic(file=file, uploadFolder=UPLOAD_FOLDER, folderName="songs")
            if ValidatorsSongs.validateField(field=imgUrl):
                songModel.setImgUrl(imgUrl=imgUrl)
                return FileImgUtils.convertSongModelWithImgBase64(songModel=self.iSongPersistencePort.createWithReferenceToAlbum(songModel))

    def getById(self, id: str) -> SongModel:
        if ValidatorsSongs.validateFieldId(id=id):
            return FileImgUtils.convertSongModelWithImgBase64(songModel=self.iSongPersistencePort.getById(id=id))

    def updateByIdWithReferenceToAlbum(self, id: str, songModel: SongModel) -> SongModel:
        if ValidatorsSongs.validateFieldId(id=id) and ValidatorsSongs.validateFields(songModel=songModel):
            return FileImgUtils.convertSongModelWithImgBase64(songModel=self.iSongPersistencePort.updateByIdWithReferenceToAlbum(id=id, songModel=songModel))

    def deleteById(self, id: str) -> str:
        if ValidatorsSongs.validateFieldId(id=id):
            return self.iSongPersistencePort.deleteById(id=id)

    def getSongsByGender(self, gender: str) -> list[SongModel]:
        if ValidatorsSongs.validateField(field=gender):
            return FileImgUtils.convertListSongModelsWithImgBase64(listSongModel=self.iSongPersistencePort.getSongsByGender(gender=gender))

    def updateImgUrlById(self, id:str, request: Request) -> SongModel:

        UPLOAD_FOLDER: str = os.path.join(os.getcwd(), 'public', 'songs')

        if (
                ValidatorsSongs.validateFieldId(id=id) and
                ValidatorsSongs.validateRequestContainFile(request=request)
        ):

            file = request.files['file']
            imageUrl: str = FileImgUtils.saveImgInDirectoryPublic(file=file, uploadFolder=UPLOAD_FOLDER, folderName="songs")
            if ValidatorsSongs.validateField(field=imageUrl):
                return FileImgUtils.convertSongModelWithImgBase64(songModel=self.iSongPersistencePort.updateImgUrlById(id=id, imageUrl=imageUrl))

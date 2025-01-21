import os
from flask import Request
from app.domain.apis.IAlbumServicePort import IAlbumServicePort
from app.domain.models.AlbumModel import AlbumModel
from app.domain.spi.IAlbumPersistencePort import IAlbumPersistencePort
from app.domain.utils.FileImgUtils import FileImgUtils
from app.domain.validators.ValidatorsAlbums import ValidatorsAlbums


class AlbumUseCase(IAlbumServicePort):

    def __init__(self, iAlbumPersistencePort: IAlbumPersistencePort):
        self.iAlbumPersistencePort = iAlbumPersistencePort

    def getAll(self) -> list[AlbumModel]:
        listAlbumModels: list[AlbumModel] = self.iAlbumPersistencePort.getAll()
        return FileImgUtils.convertListAlbumModelsWithImgBase64(listAlbumModel=listAlbumModels)

    def create(self, album: AlbumModel, request: Request) -> AlbumModel:

        UPLOAD_FOLDER: str = os.path.join(os.getcwd(), 'public', 'albums')

        if (
            ValidatorsAlbums.validateFormatToDateCreation(dateCreation=album.getDateCreation()) and
            ValidatorsAlbums.validateRequestContainFile(request=request) and
            ValidatorsAlbums.validateFields(albumModel=album)
        ):
            file = request.files['file']
            imageUrl: str = FileImgUtils.saveImgInDirectoryPublic(file=file, uploadFolder=UPLOAD_FOLDER, folderName="albums")
            if ValidatorsAlbums.validateField(field=imageUrl):
                album.setImageUrl(imageUrl=imageUrl)
                albumModelCreated: AlbumModel = self.iAlbumPersistencePort.create(album=album)
                return FileImgUtils.convertAlbumModelWithImgBase64(albumModel=albumModelCreated)

    def getById(self, id: str) -> AlbumModel:
        if ValidatorsAlbums.validateId(id):
            return FileImgUtils.convertAlbumModelWithImgBase64(albumModel=self.iAlbumPersistencePort.getById(id=id))


    def updateSingleDataById(self, id: str, album: AlbumModel) -> AlbumModel:
        if (
                ValidatorsAlbums.validateId(id)
                and ValidatorsAlbums.validateFields(albumModel=album)
                and ValidatorsAlbums.validateFormatToDateCreation(dateCreation=album.getDateCreation())
        ):
            return FileImgUtils.convertAlbumModelWithImgBase64(albumModel=self.iAlbumPersistencePort.updateSingleDataById(id=id, album=album))

    def deleteById(self, id: str) -> str:
        if ValidatorsAlbums.validateId(id):
            return self.iAlbumPersistencePort.deleteById(id=id)

    def updateImgUrlSingleDataById(self, id:str, request: Request) -> AlbumModel:

        UPLOAD_FOLDER: str = os.path.join(os.getcwd(), 'public', 'albums')

        if (
                ValidatorsAlbums.validateId(id) and
                ValidatorsAlbums.validateRequestContainFile(request=request)
        ):
            file = request.files['file']
            imageUrl: str = FileImgUtils.saveImgInDirectoryPublic(file=file, uploadFolder=UPLOAD_FOLDER, folderName="albums")
            if ValidatorsAlbums.validateField(field=imageUrl):
                return FileImgUtils.convertAlbumModelWithImgBase64(albumModel=self.iAlbumPersistencePort.updateImgUrlSingleDataById(id=id, imageUrl=imageUrl))
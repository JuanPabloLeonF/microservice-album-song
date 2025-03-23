from app.src.application.dto.request_album import AlbumRequest
from app.src.application.dto.response_album import AlbumResponse
from app.src.application.mappers.i_mapper_album_application import IMapperAlbumApplication
from app.src.domain.models.album_model import AlbumModel
from app.src.domain.services.i_service_album import IAlbumService
from app.src.application.handlers.i_handler_album import IAlbumHandler
from app.src.application.utils.utils_file_application import UtilsFilesApplication

class ImplementationAlbumHandler(IAlbumHandler):

    def __init__(self, iMapperAlbumApplication: IMapperAlbumApplication, iAlbumService: IAlbumService):
        self.iMapperAlbumApplication: IMapperAlbumApplication = iMapperAlbumApplication
        self.iAlbumService: IAlbumService = iAlbumService

    async def getAll(self, page: int, limit: int) -> list[AlbumResponse]:
        response: list[AlbumResponse] = self.iMapperAlbumApplication.mapperListAlbumModelToAlbumResponse(
            listAlbumModel=await self.iAlbumService.getAll(page=page, limit=limit)
        )

        responseDict: list[AlbumResponse] = self.iMapperAlbumApplication.mapperListResponseAlbumToListResponseAlbumDict(
            listAlbumResponse=response)

        return responseDict

    async def getById(self, id: str) -> AlbumResponse:
        response: AlbumResponse = self.iMapperAlbumApplication.mapperAlbumModelToAlbumResponse(
            albumModel=await self.iAlbumService.getById(id=id)
        )

        responseDict: AlbumResponse = self.iMapperAlbumApplication.mapperResponseAlbumToResponseAlbumDict(
            albumResponse=response
        )

        return responseDict

    async def getByAuthor(self, author: str, page: int, limit: int) -> list[AlbumResponse]:
        response: list[AlbumResponse] = self.iMapperAlbumApplication.mapperListAlbumModelToAlbumResponse(
            listAlbumModel= await self.iAlbumService.getByAuthor(author=author, page=page, limit=limit)
        )

        return [album.getJSON() for album in response]

    async def create(self, request: AlbumRequest) -> AlbumResponse:
        imgUrl: str = UtilsFilesApplication.saveFile(file=request.getImageFile(), folderName="files/albums/images")
        albumModel: AlbumModel = self.iMapperAlbumApplication.mapperRequestAlbumToAlbumModel(request=request, imgUrlAlbum=imgUrl)
        albumResponse: AlbumResponse = self.iMapperAlbumApplication.mapperAlbumModelToAlbumResponse(
            albumModel=await self.iAlbumService.create(albumModel=albumModel)
        )
        return albumResponse.getJSON()

    async def updateById(self, id: str, request: AlbumRequest) -> AlbumResponse:
        imgUrl: str = UtilsFilesApplication.saveFile(file=request.getImageFile(), folderName="files/albums/images")
        albumModel: AlbumModel = self.iMapperAlbumApplication.mapperRequestAlbumToAlbumModel(request=request, imgUrlAlbum=imgUrl)
        albumResponse: AlbumResponse = self.iMapperAlbumApplication.mapperAlbumModelToAlbumResponse(
            albumModel=await self.iAlbumService.updateById(id=id, albumUpdate=albumModel)
        )

        responseDict: AlbumResponse = self.iMapperAlbumApplication.mapperResponseAlbumToResponseAlbumDict(
            albumResponse=albumResponse
        )

        return responseDict

    async def deleteById(self, id: str) -> str:
        return await self.iAlbumService.deleteById(id=id)
from app.src.application.dto.response_song import ResponseSong
from app.src.domain.models.song_model import SongModel
from app.src.domain.services.i_service_song import ISongService
from app.src.application.dto.request_song import RequestSong
from app.src.application.mappers.i_mapper_song_application import IMapperSongApplication
from app.src.application.handlers.i_handler_song import ISongHandler
from app.src.application.utils.utils_file_application import UtilsFilesApplication

class ImplementationSongHandler(ISongHandler):

    def __init__(self, iMapperSongApplication: IMapperSongApplication, iSongService: ISongService):
        self.iSongService: ISongService = iSongService
        self.iMapperSongApplication: IMapperSongApplication = iMapperSongApplication

    async def getAll(self, page: int, limit: int) -> list[ResponseSong]:
        return self.iMapperSongApplication.mapperListSongModelToListResponseSong(
             listSongModel=await self.iSongService.getAll(page=page, limit=limit)
        )

    async def getById(self, id: str) -> ResponseSong:
        return self.iMapperSongApplication.mapperSongModelToResponseSong(
            songModel= await self.iSongService.getById(id=id)
        )

    async def getByGender(self, gender: str, page: int, limit: int) -> list[ResponseSong]:
        return self.iMapperSongApplication.mapperListSongModelToListResponseSong(
            listSongModel= await self.iSongService.getByGender(gender=gender, page=page, limit=limit)
        )

    async def create(self, request: RequestSong) -> ResponseSong:
        imgCoverUrl: str = UtilsFilesApplication.saveFile(file=request.imgCoverFile, folderName="files/images")
        musicUrl: str = UtilsFilesApplication.saveFile(file=request.musicFile, folderName="files/music")
        songModel: SongModel = self.iMapperSongApplication.mapperRequestSongToSongModel(requestSong=request, imgCoverUrl=imgCoverUrl, musicUrl=musicUrl)
        songResponse: ResponseSong = self.iMapperSongApplication.mapperSongModelToResponseSong(
            songModel=await self.iSongService.create(song=songModel)
        )
        return songResponse.getJSON()

    async def updateById(self, request: RequestSong, id: str) -> ResponseSong:
        imgCoverUrl: str = UtilsFilesApplication.saveFile(file=request.imgCoverFile, folderName="files/images")
        musicUrl: str = UtilsFilesApplication.saveFile(file=request.musicFile, folderName="files/music")
        songModel: SongModel = self.iMapperSongApplication.mapperRequestSongToSongModel(requestSong=request, imgCoverUrl=imgCoverUrl, musicUrl=musicUrl)
        songResponse: ResponseSong = self.iMapperSongApplication.mapperSongModelToResponseSong(
            songModel=await self.iSongService.updateById(song=songModel, id=id)
        )
        return songResponse.getJSON()

    async def deleteById(self, id: str) -> str:
        return await self.iSongService.deleteById(id=id)
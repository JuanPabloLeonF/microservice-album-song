from flask import jsonify, Response
from app.application.dtos.SongResponse import SongResponse
from app.application.handlers.ISongHandler import ISongHandler
from app.application.mappers.ISongRequestMapper import ISongRequestMapper
from app.application.mappers.ISongResponseMapper import ISongResponseMapper
from app.domain.apis.ISongServicePort import ISongServicePort
from app.domain.models.SongModel import SongModel
from flask import Request

class SongHandlerImplementation(ISongHandler):

    def __init__(self, iSongServicePort: ISongServicePort, iSongResponseMapper: ISongResponseMapper, iSongRequestMapper: ISongRequestMapper):
        self.iSongServicePort: ISongServicePort = iSongServicePort
        self.iSongResponseMapper: ISongResponseMapper = iSongResponseMapper
        self.iSongRequestMapper: ISongRequestMapper = iSongRequestMapper

    def getAll(self) -> tuple[Response, int]:
        songDataBase: list[SongModel] = self.iSongServicePort.getAll()
        songResponseList: list[SongResponse] = self.iSongResponseMapper.mapperSongModelListToSongResponseList(songDataBase)
        songResponseListEndpoint: list[dict] = [songResponse.getJSON() for songResponse in songResponseList]
        return jsonify(songResponseListEndpoint), 200

    def createWithReferenceToAlbum(self, request: Request) -> tuple[Response, int]:
        songRequest: SongModel = self.iSongRequestMapper.mapperRequestDataToSongModel(request)
        songModel: SongModel = self.iSongServicePort.createWithReferenceToAlbum(songModel=songRequest, request=request)
        songResponse: SongResponse = self.iSongResponseMapper.mapperSongModelToSongResponse(songModel)
        return jsonify(songResponse.getJSON()), 201

    def getById(self, id: str) -> tuple[Response, int]:
        songModel: SongModel = self.iSongServicePort.getById(id)
        songResponse: SongResponse = self.iSongResponseMapper.mapperSongModelToSongResponse(songModel)
        return jsonify(songResponse.getJSON()), 200

    def updateByIdWithReferenceToAlbum(self, id: str, request: dict) -> tuple[Response, int]:
        songRequest: SongModel = self.iSongRequestMapper.mapperRequestDataToSongModelUpdate(request)
        songModel: SongModel = self.iSongServicePort.updateByIdWithReferenceToAlbum(id, songRequest)
        songResponse: SongResponse = self.iSongResponseMapper.mapperSongModelToSongResponse(songModel)
        return jsonify(songResponse.getJSON()), 200

    def deleteById(self, id: str) -> tuple[Response, int]:
        return jsonify({
            "message": self.iSongServicePort.deleteById(id)
        }), 204

    def getSongsByGender(self, gender: str) -> tuple[Response, int]:
        songModelList: list[SongModel] = self.iSongServicePort.getSongsByGender(gender)
        songResponseList: list[SongResponse] = self.iSongResponseMapper.mapperSongModelListToSongResponseList(songModelList)
        songResponseListEndpoint: list[dict] = [songResponse.getJSON() for songResponse in songResponseList]
        return jsonify(songResponseListEndpoint), 200

    def updateImgUrlById(self, id: str, request: Request) -> tuple[Response, int]:
        songModel = self.iSongServicePort.updateImgUrlById(id=id, request=request)
        songResponse: SongResponse = self.iSongResponseMapper.mapperSongModelToSongResponse(songModel)
        return jsonify(songResponse.getJSON()), 200
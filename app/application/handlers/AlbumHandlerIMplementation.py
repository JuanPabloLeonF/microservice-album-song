from flask import jsonify, Response, Request

from app.application.dtos.AlbumResponse import AlbumResponse
from app.application.handlers.IAlbumHandler import IAlbumHandler
from app.application.mappers import IAlbumRequestMapper
from app.application.mappers.IAlbumResponseMapper import IAlbumResponseMapper
from app.domain.apis.IAlbumServicePort import IAlbumServicePort
from app.domain.models.AlbumModel import AlbumModel


class AlbumHandlerImplementation(IAlbumHandler):

    def __init__(self, iAlbumServicePort: IAlbumServicePort, iAlbumResponseMapper: IAlbumResponseMapper, iAlbumRequestMapper: IAlbumRequestMapper):
        self.iAlbumServicePort: IAlbumServicePort = iAlbumServicePort
        self.iAlbumResponseMapper: IAlbumResponseMapper = iAlbumResponseMapper
        self.iAlbumRequestMapper: IAlbumRequestMapper = iAlbumRequestMapper

    def getAll(self) -> tuple[Response, int]:
        albumDataBase: list[AlbumModel] = self.iAlbumServicePort.getAll()
        albumResponse: list[AlbumResponse] = self.iAlbumResponseMapper.mapperAlbumModelListToAlbumResponseList(albumModelList=albumDataBase)
        albumResponseEndpoint: list[dict] = list(map(lambda album: album.getJSON(), albumResponse))
        return jsonify(albumResponseEndpoint), 200

    def create(self, request: Request) -> tuple[Response, int]:
        albumRequest: AlbumModel = self.iAlbumRequestMapper.mapperRequestDataToAlbumModel(request)
        albumDataBase: AlbumModel = self.iAlbumServicePort.create(album=albumRequest, request=request)
        albumResponse: AlbumResponse = self.iAlbumResponseMapper.mapperAlbumModelToAlbumResponse(albumModel=albumDataBase)
        return jsonify(albumResponse.getJSON()), 200

    def getById(self, id: str) -> tuple[Response, int]:
        albumDataBase: AlbumModel = self.iAlbumServicePort.getById(id)
        albumResponse: AlbumResponse = self.iAlbumResponseMapper.mapperAlbumModelToAlbumResponse(albumModel=albumDataBase)
        return jsonify(albumResponse.getJSON()), 200

    def updateSingleDataById(self, id: str, request: dict) -> tuple[Response, int]:
        albumRequest: AlbumModel = self.iAlbumRequestMapper.mapperAlbumModelToAlbumModelUpdate(request)
        albumDataBase: AlbumModel = self.iAlbumServicePort.updateSingleDataById(id, albumRequest)
        albumResponse: AlbumResponse = self.iAlbumResponseMapper.mapperAlbumModelToAlbumResponse(albumModel=albumDataBase)
        return jsonify(albumResponse.getJSON()), 200

    def deleteById(self, id: str) -> tuple[Response, int]:
        return jsonify({
            "message": self.iAlbumServicePort.deleteById(id)
        }), 204

    def updateImgUrlSingleDataById(self, id:str, request: Request) -> tuple[Response, int]:
        albumDataBase: AlbumModel = self.iAlbumServicePort.updateImgUrlSingleDataById(id=id, request=request)
        albumResponse: AlbumResponse = self.iAlbumResponseMapper.mapperAlbumModelToAlbumResponse(albumModel=albumDataBase)
        return jsonify(albumResponse.getJSON()), 200
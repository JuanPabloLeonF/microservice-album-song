import injector
import json
from flask import Blueprint, request
from configurationApp.AppSongModule import AppSongModule
from app.application.handlers.ISongHandler import ISongHandler

songRoute = Blueprint('songs', __name__, url_prefix='/songs')
iSongHandler = injector.Injector([AppSongModule]).get(ISongHandler)

class SongRestController:

    @staticmethod
    @songRoute.route("/getAll", methods=['GET'])
    def getAll():
        return iSongHandler.getAll()

    @staticmethod
    @songRoute.route("/createWithReferenceToAlbum", methods=['POST'])
    def createWithReferenceToAlbum():
        return iSongHandler.createWithReferenceToAlbum(request=request)

    @staticmethod
    @songRoute.route("/getById/<id>", methods=['GET'])
    def getById(id):
        return iSongHandler.getById(id=id)

    @staticmethod
    @songRoute.route("/updateByIdWithReferenceToAlbum/<id>", methods=['PUT'])
    def updateByIdWithReferenceToAlbum(id):
        data = json.loads(request.data)
        return iSongHandler.updateByIdWithReferenceToAlbum(id=id, request=data)

    @staticmethod
    @songRoute.route("/deleteById/<id>", methods=['DELETE'])
    def deleteById(id):
        return iSongHandler.deleteById(id=id)

    @staticmethod
    @songRoute.route("/getSongsByGender/<gender>", methods=['GET'])
    def getSongsByGender(gender):
        return iSongHandler.getSongsByGender(gender=gender)

    @staticmethod
    @songRoute.route("/updateImgUrlById/<id>", methods=['PATCH'])
    def updateImgUrlById(id):
        return iSongHandler.updateImgUrlById(id=id, request=request)
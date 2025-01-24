import injector
import json
from flask import Blueprint, request

from app.application.handlers.IAlbumHandler import IAlbumHandler
from app.configurationApp.AppAlbumModule import AppAlbumModule

albumRoute = Blueprint('albums', __name__, url_prefix='/albums')
iAlbumHandler = injector.Injector([AppAlbumModule]).get(IAlbumHandler)

class AlbumRestController:

    @staticmethod
    @albumRoute.route("/getAll", methods=['GET'])
    def getAll():
        return iAlbumHandler.getAll()

    @staticmethod
    @albumRoute.route("/create", methods=['POST'])
    def create():
        return iAlbumHandler.create(request=request)

    @staticmethod
    @albumRoute.route("/getById/<id>", methods=['GET'])
    def getById(id):
        return iAlbumHandler.getById(id=id)

    @staticmethod
    @albumRoute.route("/updateSingleDataById/<id>", methods=['PUT'])
    def updateSingleDataById(id):
        data = json.loads(request.data)
        return iAlbumHandler.updateSingleDataById(id=id, request=data)

    @staticmethod
    @albumRoute.route("/deleteById/<id>", methods=['DELETE'])
    def deleteById(id):
        return iAlbumHandler.deleteById(id=id)

    @staticmethod
    @albumRoute.route("/updateImgUrlSingleDataById/<id>", methods=["PATCH"])
    def updateImgUrlSingleDataById(id):
        return iAlbumHandler.updateImgUrlSingleDataById(id=id, request=request)
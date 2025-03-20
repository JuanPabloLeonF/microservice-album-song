import injector
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.configuration.module_injector_user import ModuleInjectorSong
from app.src.application.dto.request_song import RequestSong
from app.src.application.dto.response_song import ResponseSong
from app.src.infrastructure.inputs.rest.dto.request_song_controller import SongRequestForm
from app.src.infrastructure.inputs.rest.mappers.i_mapper_song_controller import IMapperSongController
from app.src.application.handlers.i_handler_song import ISongHandler

songRouter: APIRouter = APIRouter(prefix="/song")
iHandler: ISongHandler = injector.Injector([ModuleInjectorSong()]).get(ISongHandler)
iMapperSongController: IMapperSongController =IMapperSongController()

class SongController:

    @staticmethod
    @songRouter.post("/all/{page}/{limit}", status_code=200)
    async def getAll(page: int, limit: int):
        response: list[ResponseSong] = await iHandler.getAll(page=page, limit=limit)
        return JSONResponse(content=response, status_code=200)

    @staticmethod
    @songRouter.get("/gender/{gender}/{page}/{limit}", status_code=200)
    async def getByGender(gender: str, page: int, limit: int):
        response: list[ResponseSong] = await iHandler.getByGender(gender=gender, page=page, limit=limit)
        return JSONResponse(content=response, status_code=200)

    @staticmethod
    @songRouter.get("/id/{id}", status_code=200)
    async def getById(id: str):
        response: ResponseSong = await iHandler.getById(id=id)
        return JSONResponse(content=response, status_code=200)

    @staticmethod
    @songRouter.post("/create", status_code=201)
    async def create(request: SongRequestForm = Depends(SongRequestForm)):
        requestSong: RequestSong = iMapperSongController.mapperSongRequestFormToRequestSong(request)
        response: ResponseSong = await iHandler.create(request=requestSong)
        return JSONResponse(content=response, status_code=201)

    @staticmethod
    @songRouter.put("/update/{id}", status_code=200)
    async def updateById(id: str, request: SongRequestForm = Depends(SongRequestForm)):
        requestSong: RequestSong = iMapperSongController.mapperSongRequestFormToRequestSong(request)
        response: ResponseSong = await iHandler.updateById(request=requestSong, id=id)
        return JSONResponse(content=response, status_code=200)

    @staticmethod
    @songRouter.delete("/delete/{id}", status_code=200)
    async def deleteById(id: str):
        response: str = await iHandler.deleteById(id=id)
        return JSONResponse(content=response, status_code=200)

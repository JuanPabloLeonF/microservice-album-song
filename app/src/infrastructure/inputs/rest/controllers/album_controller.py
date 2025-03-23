import injector
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.configuration.module_injector_album import ModuleInjectorAlbum
from app.src.application.dto.request_album import AlbumRequest
from app.src.application.dto.response_album import AlbumResponse
from app.src.infrastructure.inputs.rest.dto.request_album_controller import AlbumRequestForm
from app.src.infrastructure.inputs.rest.mappers.i_mapper_album_controller import IMapperAlbumController
from app.src.application.handlers.i_handler_album import IAlbumHandler

albumRouter: APIRouter = APIRouter(prefix="/album")
iHandler: IAlbumHandler = injector.Injector([ModuleInjectorAlbum()]).get(IAlbumHandler)
iMapperAlbumController: IMapperAlbumController =IMapperAlbumController()

class AlbumController:

    @staticmethod
    @albumRouter.get("/all/{page}/{limit}", status_code=200)
    async def getAll(page: int, limit: int):
        response: list[AlbumResponse] = await iHandler.getAll(page=page, limit=limit)
        return JSONResponse(content=response, status_code=200)

    @staticmethod
    @albumRouter.get("/getById/{id}", status_code=200)
    async def getById(id: str):
        response: AlbumResponse = await iHandler.getById(id=id)
        return JSONResponse(content=response, status_code=200)

    @staticmethod
    @albumRouter.get("/author/{author}/{page}/{limit}", status_code=200)
    async def getByAuthor(author: str, page: int, limit: int):
        response: list[AlbumResponse] = await iHandler.getByAuthor(author=author, page=page, limit=limit)
        return JSONResponse(content=response, status_code=200)

    @staticmethod
    @albumRouter.post("/create", status_code=201)
    async def create(request: AlbumRequestForm = Depends(AlbumRequestForm)):
        requestAlbum: AlbumRequest = iMapperAlbumController.mapperAlbumRequestFormToRequestAlbum(albumRequestForm=request)
        response: AlbumResponse = await iHandler.create(request=requestAlbum)
        return JSONResponse(content=response, status_code=201)

    @staticmethod
    @albumRouter.put("/updateById/{id}", status_code=200)
    async def updateById(id: str, request: AlbumRequestForm = Depends(AlbumRequestForm)):
        requestAlbum: AlbumRequest = iMapperAlbumController.mapperAlbumRequestFormToRequestAlbum(albumRequestForm=request)
        response: AlbumResponse = await iHandler.updateById(id=id, request=requestAlbum)
        return JSONResponse(content=response, status_code=200)

    @staticmethod
    @albumRouter.delete("/deleteById/{id}", status_code=200)
    async def deleteById(id: str):
        response: str = await iHandler.deleteById(id=id)
        return JSONResponse(content=response, status_code=200)
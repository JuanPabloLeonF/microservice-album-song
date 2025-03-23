from app.src.domain.models.album_model import AlbumModel
from app.src.domain.services.i_service_album import IAlbumService
from app.src.domain.persistence.i_persistence_album import IAlbumPersistence

class UseCaseAlbum(IAlbumService):

    def __init__(self, iAlbumPersistence: IAlbumPersistence):
        self.iAlbumPersistence: IAlbumPersistence = iAlbumPersistence

    async def getAll(self, page: int, limit: int) -> list[AlbumModel]:
        return await self.iAlbumPersistence.getAll(page=page, limit=limit)

    async def getById(self, id: str) -> AlbumModel:
        return await self.iAlbumPersistence.getById(id=id)

    async def getByAuthor(self, author: str, page: int, limit: int) -> list[AlbumModel]:
        return await self.iAlbumPersistence.getByAuthor(author=author, page=page, limit=limit)

    async def create(self, albumModel: AlbumModel) -> AlbumModel:
        return await self.iAlbumPersistence.create(albumModel=albumModel)

    async def updateById(self, id: str, albumUpdate: AlbumModel) -> AlbumModel:
        return await self.iAlbumPersistence.updateById(id=id, albumUpdate=albumUpdate)

    async def deleteById(self, id: str) -> str:
        return await self.iAlbumPersistence.deleteById(id=id)
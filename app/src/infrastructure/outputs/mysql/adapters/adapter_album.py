from app.src.domain.persistence.i_persistence_album import IAlbumPersistence
from app.src.domain.models.album_model import AlbumModel
from app.src.infrastructure.outputs.mysql.mappers.i_mapper_album_entity import IMapperAlbumEntity
from app.src.infrastructure.outputs.mysql.repositories.i_album_repository import IAlbumRepository

class AdapterAlbum(IAlbumPersistence):

    def __init__(self, iAlbumRepository: IAlbumRepository, iMapperAlbumEntity: IMapperAlbumEntity):
        self.iAlbumRepository: IAlbumRepository = iAlbumRepository
        self.iMapperAlbumEntity: IMapperAlbumEntity = iMapperAlbumEntity

    async def getAll(self, page: int, limit: int) -> list[AlbumModel]:
        return self.iMapperAlbumEntity.mapperListAlbumEntityToListAlbumModel(
            listAlbumEntity=await self.iAlbumRepository.getAll(page=page, limit=limit)
        )

    async def getById(self, id: str) -> AlbumModel:
        return self.iMapperAlbumEntity.mapperAlbumEntityToAlbumModel(
            albumEntity= await self.iAlbumRepository.getById(id=id)
        )

    async def getByAuthor(self, author: str, page: int, limit: int) -> list[AlbumModel]:
        return self.iMapperAlbumEntity.mapperListAlbumEntityToListAlbumModel(
            listAlbumEntity= await self.iAlbumRepository.getByAuthor(author=author, page=page, limit=limit)
        )

    async def create(self, albumModel: AlbumModel) -> AlbumModel:
        return self.iMapperAlbumEntity.mapperAlbumEntityToAlbumModel(
            albumEntity= await self.iAlbumRepository.create(
                albumEntity= self.iMapperAlbumEntity.mapperAlbumModelToAlbumEntity(albumModel=albumModel)
            )
        )

    async def updateById(self, id: str, albumUpdate: AlbumModel) -> AlbumModel:
        return self.iMapperAlbumEntity.mapperAlbumEntityToAlbumModel(
            albumEntity=await self.iAlbumRepository.updateById(
                id=id,
                albumUpdate=self.iMapperAlbumEntity.mapperAlbumModelToAlbumEntity(albumModel=albumUpdate)
            )
        )

    async def deleteById(self, id: str) -> str:
        return await self.iAlbumRepository.deleteById(id=id)
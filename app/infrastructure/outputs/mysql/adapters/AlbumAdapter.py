from app.domain.models.AlbumModel import AlbumModel
from app.domain.spi.IAlbumPersistencePort import IAlbumPersistencePort
from app.infrastructure.outputs.mysql.entities.AlbumEntity import AlbumEntity
from app.infrastructure.outputs.mysql.mappers.IAlbumEntityMapper import IAlbumEntityMapper
from app.infrastructure.outputs.mysql.repository.IAlbumRepository import IAlbumRepository


class AlbumAdapter(IAlbumPersistencePort):

    def __init__(self, iAlbumRepository: IAlbumRepository, iAlbumEntityMapper: IAlbumEntityMapper):
        self.iAlbumRepository: IAlbumRepository = iAlbumRepository
        self.iAlbumEntityMapper: IAlbumEntityMapper = iAlbumEntityMapper

    def getAll(self) -> list[AlbumModel]:
        listDataBase: list[AlbumEntity] = self.iAlbumRepository.getALl()
        return self.iAlbumEntityMapper.mapperAlbumEntityListToAlbumModelList(listDataBase)

    def create(self, album: AlbumModel) -> AlbumModel:
        albumEntity: AlbumEntity = self.iAlbumEntityMapper.mapperAlbumModelToAlbumEntity(albumModel=album)
        albumDataBase: AlbumEntity = self.iAlbumRepository.create(albumEntity)
        return self.iAlbumEntityMapper.mapperAlbumEntityToAlbumModel(albumDataBase)

    def getById(self, id: str) -> AlbumModel:
        albumEntity: AlbumEntity = self.iAlbumRepository.getById(id=id)
        return self.iAlbumEntityMapper.mapperAlbumEntityToAlbumModel(albumEntity)

    def updateSingleDataById(self, id: str, album: AlbumModel) -> AlbumModel:
        albumEntity: AlbumEntity = self.iAlbumEntityMapper.mapperAlbumModelToAlbumEntity(albumModel=album)
        albumDataBase: AlbumEntity = self.iAlbumRepository.updateSingleDataById(id=id, album=albumEntity)
        return self.iAlbumEntityMapper.mapperAlbumEntityToAlbumModel(albumDataBase)

    def deleteById(self, id: str) -> str:
        return self.iAlbumRepository.deleteById(id=id)

    def updateImgUrlSingleDataById(self, id: str, imageUrl: str) -> AlbumModel:
        albumDataBase: AlbumEntity = self.iAlbumRepository.updateImgUrlSingleDataById(id=id, imageUrl=imageUrl)
        return self.iAlbumEntityMapper.mapperAlbumEntityToAlbumModel(albumDataBase)
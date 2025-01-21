from app.domain.spi.ISongPersistencePort import ISongPersistencePort
from app.infrastructure.outputs.sqlites.repository.ISongRepository import ISongRepository
from app.infrastructure.outputs.sqlites.mappers.ISongEntityMapper import ISongEntityMapper
from app.domain.models.SongModel import SongModel
from app.infrastructure.outputs.sqlites.entities.SongEntity import SongEntity

class SongAdapter(ISongPersistencePort):

    def __init__(self, iSongRepository: ISongRepository, iSongEntityMapper: ISongEntityMapper):
        self.iSongRepository: ISongRepository = iSongRepository
        self.iSongEntityMapper: ISongEntityMapper = iSongEntityMapper

    def getAll(self) -> list[SongModel]:
        listDataBase: list[SongEntity] = self.iSongRepository.getAll()
        return self.iSongEntityMapper.mapperSongEntityListToSongModelList(listDataBase)

    def createWithReferenceToAlbum(self, song: SongModel) -> SongModel:
        songEntity: SongEntity = self.iSongRepository.createWithReferenceToAlbum(song=song)
        return self.iSongEntityMapper.mapperSongEntityToSongModel(songEntity=songEntity)

    def getById(self, id: str) -> SongModel:
        songEntity: SongEntity = self.iSongRepository.getById(id=id)
        return self.iSongEntityMapper.mapperSongEntityToSongModel(songEntity=songEntity)

    def updateByIdWithReferenceToAlbum(self, id: str, songModel: SongModel) -> SongModel:
        songMapperModel: SongEntity = self.iSongEntityMapper.mapperSongModelToSongEntity(songModel=songModel)
        songEntity: SongEntity = self.iSongRepository.updateByIdWithReferenceToAlbum(id=id, songEntity=songMapperModel)
        return self.iSongEntityMapper.mapperSongEntityToSongModel(songEntity=songEntity)

    def deleteById(self, id: str) -> str:
        return self.iSongRepository.deleteById(id=id)

    def getSongsByGender(self, gender: str) -> list[SongModel]:
        listDataBase: list[SongEntity] = self.iSongRepository.getSongsByGender(gender=gender)
        return self.iSongEntityMapper.mapperSongEntityListToSongModelList(listDataBase)

    def updateImgUrlById(self, id: str, imageUrl: str) -> SongModel:
        songEntity: SongEntity = self.iSongRepository.updateImgUrlById(id=id, imageUrl=imageUrl)
        return self.iSongEntityMapper.mapperSongEntityToSongModel(songEntity=songEntity)
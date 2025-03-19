from app.src.domain.persistence.i_persistence_song import ISongPersistence
from app.src.domain.models.song_model import SongModel
from app.src.infrastructure.outputs.mysql.mappers.i_mapper_song_entity import IMapperSongEntity
from app.src.infrastructure.outputs.mysql.repositories.i_song_repository import ISongRepository

class AdapterSong(ISongPersistence):

    def __init__(self, iMapperSongEntity: IMapperSongEntity, iSongRepository: ISongRepository):
        self.iSongRepository: ISongRepository = iSongRepository
        self.iMapperSongEntity: IMapperSongEntity = iMapperSongEntity

    async def getAll(self, page: int, limit: int) -> list[SongModel]:
        return self.iMapperSongEntity.mapperListSongEntityToListSongModel(await self.iSongRepository.getAll(page=page, limit=limit))

    async def getById(self, id: str) -> SongModel:
        return self.iMapperSongEntity.mapperSongEntityToSongModel(await self.iSongRepository.getById(id=id))

    async def getByGender(self, gender: str, page: int, limit: int) -> list[SongModel]:
        return self.iMapperSongEntity.mapperListSongEntityToListSongModel(await self.iSongRepository.getByGender(gender=gender, page=page, limit=limit))

    async def create(self, song: SongModel) -> SongModel:
        return self.iMapperSongEntity.mapperSongEntityToSongModel(
            await self.iSongRepository.create(
                song=self.iMapperSongEntity.mapperSongModelToSongEntity(songModel=song)
            )
        )

    async def updateById(self, song: SongModel, id: str) -> SongModel:
        return self.iMapperSongEntity.mapperSongEntityToSongModel(
            await self.iSongRepository.updateById(
                song=self.iMapperSongEntity.mapperSongModelToSongEntity(songModel=song),
                id=id
            )
        )

    async def deleteById(self, id: str) -> str:
        return await self.iSongRepository.deleteById(id=id)
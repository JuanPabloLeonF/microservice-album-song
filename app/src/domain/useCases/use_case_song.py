from app.src.domain.models.song_model import SongModel
from app.src.domain.persistence.i_persistence_song import ISongPersistence
from app.src.domain.services.i_service_song import ISongService

class UseCaseSong(ISongService):

    def __init__(self, iSongPersistence: ISongPersistence):
        self.iSongPersistence: ISongPersistence = iSongPersistence

    async def getAll(self, page: int, limit: int) -> list[SongModel]:
        return await self.iSongPersistence.getAll(page=page, limit=limit)

    async def getById(self, id: str) -> SongModel:
        return await self.iSongPersistence.getById(id=id)

    async def getByGender(self, gender: str, page: int, limit: int) -> list[SongModel]:
        return await self.iSongPersistence.getByGender(gender=gender, page=page, limit=limit)

    async def create(self, song: SongModel) -> SongModel:
        return await self.iSongPersistence.create(song=song)

    async def updateById(self, song: SongModel, id: str) -> SongModel:
        return await self.iSongPersistence.updateById(song=song, id=id)

    async def deleteById(self, id: str) -> str:
        return await self.iSongPersistence.deleteById(id=id)
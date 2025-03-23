from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.src.infrastructure.outputs.mysql.entities.album_entity import AlbumEntity
from app.src.infrastructure.outputs.mysql.entities.song_entity import SongEntity
from app.src.infrastructure.outputs.mysql.repositories.i_song_repository import ISongRepository
from app.src.infrastructure.outputs.mysql.settings.database_config import DatabaseConfiguration
from app.src.application.utils.utils_file_application import UtilsFilesApplication

class ImplementationSongRepository(ISongRepository):

    async def getAll(self, page: int, limit: int) -> list[SongEntity]:
        async with DatabaseConfiguration.getSession() as session:
            result = await session.execute(
                select(SongEntity).
                limit(limit).
                offset((page - 1) * limit)
            )
            listSongs = result.scalars().all()
            return [song for song in listSongs]

    async def getByGender(self, gender: str, page: int, limit: int) -> list[SongEntity]:
        async with DatabaseConfiguration.getSession() as session:
            result = await session.execute(
                select(SongEntity).
                where(SongEntity.gender.contains(gender)).
                limit(limit).
                offset((page - 1) * limit)
            )
            listSongs = result.scalars().all()
            return [song for song in listSongs]

    async def getById(self, id: str) -> SongEntity:
        async with DatabaseConfiguration.getSession() as session:
            result: SongEntity | None = await session.get(SongEntity, id)
            if result is None:
                raise ValueError(f"song not found with the id: {id}")
            return result

    async def create(self, song: SongEntity) -> SongEntity:
        async with DatabaseConfiguration.getSession() as session:
            try:

                albumExist = await session.get(AlbumEntity, song.albumId)
                if not albumExist:
                    UtilsFilesApplication.deletedFile(filePath=song.imgCoverUrl)
                    UtilsFilesApplication.deletedFile(filePath=song.musicUrl)
                    raise ValueError(f"album not found with the id: {song.albumId}")

                session.add(song)
                await session.commit()
                await session.refresh(song)
                return song
            except IntegrityError as error:
                await session.rollback()
                raise ValueError(str(error))
            except SQLAlchemyError as error:
                await session.rollback()
                raise RuntimeError(str(error))

    async def updateById(self, song: SongEntity, id: str) -> SongEntity:
        async with DatabaseConfiguration.getSession() as session:
            try:
                result: SongEntity | None = await session.get(SongEntity, id)
                if result is None:
                    UtilsFilesApplication.deletedFile(filePath=song.getMusicUrl())
                    UtilsFilesApplication.deletedFile(filePath=song.getImgCoverUrl())
                    raise ValueError(f"song not found with the id: {id}")

                UtilsFilesApplication.deletedFile(filePath=result.musicUrl)
                UtilsFilesApplication.deletedFile(filePath=result.imgCoverUrl)

                result.name = song.name
                result.singer = song.singer
                result.duration = song.duration
                result.gender = song.gender
                result.albumId = song.albumId
                result.imgCoverUrl = song.imgCoverUrl
                result.musicUrl = song.musicUrl
                await session.commit()
                await session.refresh(result)
                return result
            except IntegrityError as error:
                await session.rollback()
                raise ValueError(str(error))
            except SQLAlchemyError as error:
                await session.rollback()
                raise RuntimeError(str(error))

    async def deleteById(self, id: str) -> str:
        async with DatabaseConfiguration.getSession() as session:
            try:
                result = await session.get(SongEntity, id)
                if not result:
                    raise ValueError(f"song not found with the id: {id}")

                UtilsFilesApplication.deletedFile(filePath=result.musicUrl)
                UtilsFilesApplication.deletedFile(filePath=result.imgCoverUrl)
                await session.delete(result)
                await session.commit()
                return "Song deleted successfully"
            except IntegrityError as error:
                await session.rollback()
                raise ValueError(str(error))
            except SQLAlchemyError as error:
                await session.rollback()
                raise RuntimeError(str(error))
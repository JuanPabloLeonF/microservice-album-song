from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.src.application.utils.utils_file_application import UtilsFilesApplication
from app.src.infrastructure.outputs.mysql.repositories.i_album_repository import IAlbumRepository
from app.src.infrastructure.outputs.mysql.entities.album_entity import AlbumEntity
from app.src.infrastructure.outputs.mysql.settings.database_config import DatabaseConfiguration

class ImplementationAlbumRepository(IAlbumRepository):

    async def getAll(self, page: int, limit: int) -> list[AlbumEntity]:
        async with DatabaseConfiguration.getSession() as session:
            result = await session.execute(
                select(AlbumEntity).
                limit(limit).
                offset((page - 1) * limit)
            )
            listAlbum = result.scalars().all()
            return [album for album in listAlbum]

    async def getById(self, id: str) -> AlbumEntity:
        async with DatabaseConfiguration.getSession() as session:
            result: AlbumEntity | None = await session.get(AlbumEntity, id)
            if result is None:
                raise ValueError(f"album not found with the id: {id}")
            return result

    async def getByAuthor(self, author: str, page: int, limit: int) -> list[AlbumEntity]:
        async with DatabaseConfiguration.getSession() as session:
            result = await session.execute(
                select(AlbumEntity).
                where(AlbumEntity.author.contains(author)).
                limit(limit).
                offset((page - 1) * limit)
            )
            listAlbum = result.scalars().all()
            return [album for album in listAlbum]

    async def create(self, albumEntity: AlbumEntity) -> AlbumEntity:
        async with DatabaseConfiguration.getSession() as session:
            try:
                session.add(albumEntity)
                await session.commit()
                await session.refresh(albumEntity)
                return albumEntity
            except IntegrityError as error:
                UtilsFilesApplication.deletedFile(filePath=albumEntity.imageCoverUrl)
                await session.rollback()
                raise ValueError(str(error))
            except SQLAlchemyError as error:
                UtilsFilesApplication.deletedFile(filePath=albumEntity.imageCoverUrl)
                await session.rollback()
                raise RuntimeError(str(error))

    async def updateById(self, id: str, albumUpdate: AlbumEntity) -> AlbumEntity:
        async with DatabaseConfiguration.getSession() as session:
            try:
                result: AlbumEntity | None = await session.get(AlbumEntity, id)
                if result is None:
                    UtilsFilesApplication.deletedFile(filePath=albumUpdate.imageCoverUrl)
                    raise ValueError(f"album not found with the id: {id}")

                UtilsFilesApplication.deletedFile(filePath=result.imageCoverUrl)
                result.name = albumUpdate.name
                result.author = albumUpdate.author
                result.dateCreation = albumUpdate.dateCreation
                result.description = albumUpdate.description
                result.imageCoverUrl = albumUpdate.imageCoverUrl

                if len(result.getSongs()) <= 0:
                    result.songs = albumUpdate.songs

                result.songs = result.getSongs()
                await session.commit()
                await session.refresh(result)
                return result
            except IntegrityError as error:
                UtilsFilesApplication.deletedFile(filePath=albumUpdate.imageCoverUrl)
                await session.rollback()
                raise ValueError(str(error))
            except SQLAlchemyError as error:
                UtilsFilesApplication.deletedFile(filePath=albumUpdate.imageCoverUrl)
                await session.rollback()
                raise RuntimeError(str(error))

    async def deleteById(self, id: str) -> str:
        async with DatabaseConfiguration.getSession() as session:
            try:
                result = await session.get(AlbumEntity, id)
                if not result:
                    raise ValueError(f"album not found with the id: {id}")

                UtilsFilesApplication.deletedFile(filePath=result.imageCoverUrl)

                if len(result.songs) > 0:
                    for song in result.songs:
                        UtilsFilesApplication.deletedFile(filePath=song.musicUrl)
                        UtilsFilesApplication.deletedFile(filePath=song.imgCoverUrl)

                await session.delete(result)
                await session.commit()
                return "Album deleted successfully"
            except IntegrityError as error:
                await session.rollback()
                raise ValueError(str(error))
            except SQLAlchemyError as error:
                await session.rollback()
                raise RuntimeError(str(error))
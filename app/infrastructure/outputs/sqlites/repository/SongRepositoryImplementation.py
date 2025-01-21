from app.domain.models.SongModel import SongModel
from app.domain.utils.FileImgUtils import FileImgUtils
from app.infrastructure.exceptions.ExceptionHandlersGlobal import ValidateData
from app.infrastructure.outputs.sqlites.entities.AlbumEntity import AlbumEntity
from app.infrastructure.outputs.sqlites.repository.ISongRepository import ISongRepository
from app.infrastructure.outputs.sqlites.entities.SongEntity import SongEntity
from app.infrastructure.outputs.sqlites.configurations.DatabaseConfiguration import db

class SongRepositoryImplementation(ISongRepository):

    def getAll(self) -> list[SongEntity]:
        return SongEntity.query.all()

    def createWithReferenceToAlbum(self, song: SongModel) -> SongEntity:

        albumFound: AlbumEntity = AlbumEntity.query.get(song.getAlbumId())

        if not albumFound:
            raise ValidateData(f"El album con el id: {song.getAlbumId()} no existe")

        createSongEntity: SongEntity = SongEntity(
            name=song.getName(),
            singer=song.getSinger(),
            duration=song.getDuration(),
            gender=song.getGender(),
            imgUrl=song.getImgUrl(),
            albumId=song.getAlbumId()
        )

        db.session.add(createSongEntity)
        db.session.commit()
        return createSongEntity

    def getById(self, id: str) -> SongEntity:

        songEntityFound: SongEntity = SongEntity.query.get(id)

        if not songEntityFound:
            raise ValidateData(f"La cancion con el id: {id} no existe")

        return songEntityFound

    def updateByIdWithReferenceToAlbum(self, id: str, songEntity: SongEntity) -> SongEntity:

        albumFound: AlbumEntity = AlbumEntity.query.get(songEntity.albumId)

        if not albumFound:
            raise ValidateData(f"El album con el id: {songEntity.albumId} no existe")

        songEntityFound: SongEntity = SongEntity.query.get(id)

        if not songEntityFound:
            raise ValidateData(f"La cancion con el id: {id} no existe")

        songEntityFound.name = songEntity.name
        songEntityFound.singer = songEntity.singer
        songEntityFound.duration = songEntity.duration
        songEntityFound.gender = songEntity.gender
        songEntityFound.albumId = songEntity.albumId
        db.session.commit()

        return songEntityFound

    def deleteById(self, id: str) -> str:

        songEntityFound: SongEntity = SongEntity.query.get(id)

        if not songEntityFound:
            raise ValidateData(f"La cancion con el id: {id} no existe")

        FileImgUtils.deleteImgInDirectoryPublic(imageUrl=songEntityFound.imgUrl)
        db.session.delete(songEntityFound)
        db.session.commit()

        return f"La cancion con el id: {id} ha sido eliminada"

    def getSongsByGender(self, gender: str) -> list[SongEntity]:
        return SongEntity.query.filter(SongEntity.gender.like(f'%"{gender}"%')).all()

    def updateImgUrlById(self, id: str, imageUrl: str) -> SongEntity:
        songEntityFound: SongEntity = SongEntity.query.get(id)

        if not songEntityFound:
            FileImgUtils.deleteImgInDirectoryPublic(imageUrl=imageUrl)
            raise ValidateData(f"La cancion con el id: {id} no existe")

        FileImgUtils.deleteImgInDirectoryPublic(imageUrl=songEntityFound.imgUrl)
        songEntityFound.imgUrl = imageUrl
        db.session.commit()
        return songEntityFound
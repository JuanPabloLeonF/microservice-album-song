from app.infrastructure.exceptions.ExceptionHandlersGlobal import ValidateData
from app.infrastructure.outputs.mysql.entities.AlbumEntity import AlbumEntity
from app.infrastructure.outputs.mysql.repository.IAlbumRepository import IAlbumRepository
from app.infrastructure.outputs.mysql.configurations.DatabaseConfiguration import db
from app.domain.utils.FileImgUtils import FileImgUtils

class AlbumRepositoryImplementation(IAlbumRepository):

    def getALl(self) -> list[AlbumEntity]:
        return AlbumEntity.query.all()

    def create(self, album: AlbumEntity) -> AlbumEntity:

        createAlbumEntity: AlbumEntity = AlbumEntity(
            name=album.getName(),
            author=album.getAuthor(),
            dateCreation=album.getDateCreation(),
            description=album.getDescription(),
            imageUrl= album.getImageUrl(),
            songs=album.getSongs()
        )

        db.session.add(createAlbumEntity)
        db.session.commit()
        return createAlbumEntity

    def getById(self, id: str) -> AlbumEntity:
        albumFound: AlbumEntity = AlbumEntity.query.get(id)

        if not albumFound:
            raise ValidateData(f"El album con el id: {id} no existe")

        return albumFound

    def updateSingleDataById(self, id: str, album: AlbumEntity) -> AlbumEntity:
        albumFound: AlbumEntity = AlbumEntity.query.get(id)

        if not albumFound:
            raise ValidateData(f"El album con el id: {id} no existe")

        albumFound.name = album.getName()
        albumFound.author = album.getAuthor()
        albumFound.dateCreation = album.getDateCreation()
        albumFound.description = album.getDescription()

        db.session.commit()
        return albumFound

    def deleteById(self, id: str) -> str:

        albumFound: AlbumEntity = AlbumEntity.query.get(id)

        if not albumFound:
            raise ValidateData(f"El album con el id: {id} no existe")

        FileImgUtils.deleteImgInDirectoryPublic(imageUrl=albumFound.imageUrl)
        [FileImgUtils.deleteImgInDirectoryPublic(imageUrl=songFound.imgUrl) for songFound in albumFound.songs]
        db.session.delete(albumFound)
        db.session.commit()

        return f"El album con el id: {id} ha sido eliminado"

    def updateImgUrlSingleDataById(self, id: str, imageUrl: str) -> AlbumEntity:
        albumFound: AlbumEntity = AlbumEntity.query.get(id)

        if not albumFound:
            FileImgUtils.deleteImgInDirectoryPublic(imageUrl)
            raise ValidateData(f"El album con el id: {id} no existe")

        FileImgUtils.deleteImgInDirectoryPublic(imageUrl=albumFound.imageUrl)
        albumFound.imageUrl = imageUrl
        db.session.commit()
        return albumFound
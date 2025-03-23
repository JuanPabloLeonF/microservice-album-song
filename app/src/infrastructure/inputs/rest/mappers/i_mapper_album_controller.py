from app.src.application.dto.request_album import AlbumRequest
from app.src.infrastructure.inputs.rest.dto.request_album_controller import AlbumRequestForm

class IMapperAlbumController:

    @staticmethod
    def mapperAlbumRequestFormToRequestAlbum(albumRequestForm: AlbumRequestForm) -> AlbumRequest:
        return AlbumRequest(
            name=albumRequestForm.name,
            author=albumRequestForm.author,
            dateCreation=albumRequestForm.dateCreation,
            description=albumRequestForm.description,
            imageFile=albumRequestForm.imgFile,
        )
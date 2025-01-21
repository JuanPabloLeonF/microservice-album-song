from app.domain.models.SongModel import SongModel
from app.infrastructure.exceptions.ExceptionHandlersGlobal import ValidateData
from flask import Request


class ValidatorsSongs:

    @staticmethod
    def validateFileName(filename: str) -> bool:
        if not filename:
            raise ValidateData("El file no tiene nombre")
        return True

    @staticmethod
    def validateRequestContainFile(request: Request) -> bool:
        if 'file' not in request.files:
            raise ValidateData(f"El campo file es obligatorio")

        return True

    @staticmethod
    def validateExtensionToFile(filename) -> bool:
        ALLOWED_EXTENSIONS: set[str] = {'png', 'jpg', 'jpeg', 'webp'}
        if not '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
            raise ValidateData(f"El archivo debe ser de tipo {ALLOWED_EXTENSIONS}")
        return True


    @staticmethod
    def validateFields(songModel: SongModel) -> bool:
        if not songModel.getName():
            raise ValidateData("El campo name es obligatorio")
        elif not songModel.getSinger():
            raise ValidateData("El campo singer es obligatorio")
        elif not songModel.getDuration():
            raise ValidateData("El campo duration es obligatorio")
        elif not songModel.getGender():
            raise ValidateData("El campo gender es obligatorio")
        elif not songModel.getAlbumId():
            raise ValidateData("El campo albumId es obligatorio")

        return True

    @staticmethod
    def validateFieldId(id: str) -> bool:
        if not id:
            raise ValidateData("El campo id es obligatorio")
        return True

    @staticmethod
    def validateField(field: str) -> bool:
        if not field:
            raise ValidateData("El campo es obligatorio")
        return True
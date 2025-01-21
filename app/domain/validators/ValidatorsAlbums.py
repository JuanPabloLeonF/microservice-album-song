import re
from flask import Request
from app.domain.models.AlbumModel import AlbumModel
from app.infrastructure.exceptions.ExceptionHandlersGlobal import ValidateData


class ValidatorsAlbums:

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
    def validateFields(albumModel: AlbumModel) -> bool:
        if not albumModel.getName():
            raise ValidateData("El campo name es obligatorio")
        elif not albumModel.getAuthor():
            raise ValidateData("El campo author es obligatorio")
        elif not albumModel.getDateCreation():
            raise ValidateData("El campo dateCreation es obligatorio")
        elif not albumModel.getDescription():
            raise ValidateData("El campo description es obligatorio")

        return True

    @staticmethod
    def validateId(id: str) -> bool:
        if not id:
            raise ValidateData("El campo id es obligatorio")
        return True

    @staticmethod
    def validateFormatToDateCreation(dateCreation: str) -> bool:
        pattern = r"^\d{2}/\d{2}/\d{4}$"
        if not re.match(pattern, dateCreation):
            raise ValidateData("El campo dateCreation debe tener el formato (DD/MM/YYYY)")
        return True

    @staticmethod
    def validateField(field: str) -> bool:
        if not field:
            raise ValidateData("El campo es obligatorio")
        return True
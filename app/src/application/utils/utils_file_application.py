import os
import uuid
import base64
from fastapi import UploadFile
from app.configuration.enviroments_config import ALLOW_EXTENSIONS_FILE_IMG, ALLOW_EXTENSIONS_FILE_MUSIC, MAX_SIZE_IMG_FILE_MB, MAX_SIZE_MUSIC_FILE_MB

class UtilsFilesApplication:

    @staticmethod
    def convertFileToBase64(filePath: str) -> str:
        if not os.path.exists(filePath):
            raise ValueError("File not found")
        with open(filePath, "rb") as file:
            return base64.b64encode(file.read()).decode("utf-8")

    @staticmethod
    def createFolder(folderName: str) -> None:
        os.makedirs(name=folderName, exist_ok=True)

    @staticmethod
    def validateExtensionFile(imgUrl: str, file: UploadFile, listExtensions: list[str]) -> None:
        extension: str = UtilsFilesApplication.getExtensionsFile(file=file)
        if extension not in listExtensions:
            if imgUrl:
                UtilsFilesApplication.deletedFile(filePath=imgUrl)
            raise ValueError("Invalid file extension")

    @staticmethod
    def convertSizeToMB(file: UploadFile) -> float:
        file.file.seek(0, os.SEEK_END)
        size = file.file.tell()
        file.file.seek(0)
        return size / (1024 * 1024)

    @staticmethod
    def getExtensionsFile(file: UploadFile) -> str:
        return file.filename.split(".")[-1].lower()

    @staticmethod
    def validateMaxSizeMusicFile(file: UploadFile) -> None:
        sizeMB: float = UtilsFilesApplication.convertSizeToMB(file=file)
        if sizeMB > MAX_SIZE_MUSIC_FILE_MB:
            raise ValueError(f"Lo siento el archivo es demasiado pesado, maximo de {MAX_SIZE_MUSIC_FILE_MB}MB")

    @staticmethod
    def validateMaxSizeImgFile(file: UploadFile) -> None:
        sizeMB: float = UtilsFilesApplication.convertSizeToMB(file=file)
        if sizeMB > MAX_SIZE_IMG_FILE_MB:
            raise ValueError(f"Lo siento el archivo es demasiado pesado, maximo de {MAX_SIZE_IMG_FILE_MB}MB")

    @staticmethod
    def deletedFile(filePath: str) -> None:
        if os.path.exists(filePath):
            os.remove(filePath)

    @staticmethod
    def saveFile(file: UploadFile, folderName: str, imgUrl: str = None) -> str:

        UtilsFilesApplication.validateExtensionFile(
            imgUrl=imgUrl,
            file=file,
            listExtensions=ALLOW_EXTENSIONS_FILE_IMG + ALLOW_EXTENSIONS_FILE_MUSIC
        )

        extension: str = UtilsFilesApplication.getExtensionsFile(file=file)
        fileNameFull: str = f"{uuid.uuid4()}.{extension}"
        UtilsFilesApplication.createFolder(folderName=folderName)
        filePath: str = os.path.join(folderName, fileNameFull)

        if extension in ALLOW_EXTENSIONS_FILE_IMG:
            UtilsFilesApplication.validateMaxSizeImgFile(file=file)

        if extension in ALLOW_EXTENSIONS_FILE_MUSIC:
            UtilsFilesApplication.validateMaxSizeMusicFile(file=file)

        with open(filePath, "wb") as buffer:
            buffer.write(file.file.read())
        return filePath
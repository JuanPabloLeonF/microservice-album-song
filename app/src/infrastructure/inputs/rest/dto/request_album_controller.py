from fastapi import Form, UploadFile, File

class AlbumRequestForm:
    def __init__(
        self,
        name: str = Form(min_length=3, max_length=100),
        author: str = Form(min_length=3, max_length=100),
        dateCreation: str = Form(min_length=10, max_length=20),
        description: str = Form(min_length=3, max_length=200),
        imgFile: UploadFile = File(),
    ):
        self.name = name
        self.author = author
        self.dateCreation = dateCreation
        self.description = description
        self.imgFile = imgFile
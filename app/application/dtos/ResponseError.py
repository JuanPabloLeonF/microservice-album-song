class ResponseError:
    def __init__(self, status: str, statusCode: int, message: str):
        self.__status: str = status
        self.__statusCode: int = statusCode
        self.__message: str = message

    def getJSON(self):
        return {
            "status": self.__status,
            "statusCode": self.__statusCode,
            "message": self.__message
        }
class ResponseError:

    def __init__(self, status: str, messageError: str, statusCode: int):
        self.status: str = status
        self.messageError: str = messageError
        self.statusCode: int = statusCode

    def getJSON(self):
        return {
            "status": self.status,
            "messageError": self.messageError,
            "statusCode": self.statusCode
        }
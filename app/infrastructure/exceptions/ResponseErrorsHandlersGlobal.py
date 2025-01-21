from flask import jsonify

from app.application.dtos.ResponseError import ResponseError
from app.infrastructure.exceptions.ExceptionHandlersGlobal import ValidateData

def responseErrorsHandlersGlobal(app):

    @app.errorhandler(ValidateData)
    def handlerValidateData(error):
        responseError: ResponseError = ResponseError("BAD REQUEST", 400, str(error))
        return jsonify(responseError.getJSON()), 400
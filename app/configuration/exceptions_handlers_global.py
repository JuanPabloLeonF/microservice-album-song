from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from fastapi.responses import JSONResponse
from app.configuration.exceptions_personalities import ErrorSessionDatabase
from app.src.application.dto.response_error import ResponseError
from app.configuration.exceptions_personalities import IntegrityErrorDatabase

class ErrorsHandlersGlobals:

    @staticmethod
    def errorHandlerRequestValidationError(request: Request, exception: RequestValidationError) -> JSONResponse:
        responseError: ResponseError = ResponseError(
            status="BAD_REQUEST",
            statusCode=status.HTTP_400_BAD_REQUEST,
            messageError=str(exception)
        )
        return JSONResponse(content=responseError.getJSON(), status_code=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def errorHandlerRequestValueError(request: Request, exception: ValueError) -> JSONResponse:
        responseError: ResponseError = ResponseError(
            status="NOT_FOUND",
            statusCode=status.HTTP_404_NOT_FOUND,
            messageError=str(exception)
        )
        return JSONResponse(content=responseError.getJSON(), status_code=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def errorHandlerErrorSessionDatabase(request: Request, exception: ErrorSessionDatabase) -> JSONResponse:
        responseError: ResponseError = ResponseError(
            status="INTERNAL_SERVER_ERROR",
            statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR,
            messageError=str(exception)
        )
        return JSONResponse(content=responseError.getJSON(), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def errorHandlerIntegrityErrorDatabase(request: Request, exception: IntegrityErrorDatabase) -> JSONResponse:
        responseError: ResponseError = ResponseError(
            status="BAD_REQUEST",
            statusCode=status.HTTP_400_BAD_REQUEST,
            messageError=str(exception)
        )
        return JSONResponse(content=responseError.getJSON(), status_code=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def errorHandlerRuntimeError(request: Request, exception: RuntimeError) -> JSONResponse:
        responseError: ResponseError = ResponseError(
            status="INTERNAL_SERVER_ERROR",
            statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR,
            messageError=str(exception)
        )
        return JSONResponse(content=responseError.getJSON(), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def errorHandlerNotFound(request: Request, exception: HTTPException) -> JSONResponse:
        if exception.status_code == 404:
            responseError: ResponseError = ResponseError(
                status="NOT_FOUND",
                statusCode=status.HTTP_404_NOT_FOUND,
                messageError="La ruta que estás intentando acceder no existe"
            )
            return JSONResponse(content=responseError.getJSON(), status_code=status.HTTP_404_NOT_FOUND)
        return JSONResponse(content={"detailError": str(exception.detail)}, status_code=exception.status_code)


    @staticmethod
    def registerHandlersMethodsDict() -> dict:
        return {
            RequestValidationError: ErrorsHandlersGlobals.errorHandlerRequestValidationError,
            ValueError: ErrorsHandlersGlobals.errorHandlerRequestValueError,
            ErrorSessionDatabase: ErrorsHandlersGlobals.errorHandlerErrorSessionDatabase,
            IntegrityErrorDatabase: ErrorsHandlersGlobals.errorHandlerIntegrityErrorDatabase,
            RuntimeError: ErrorsHandlersGlobals.errorHandlerRuntimeError
        }
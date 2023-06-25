import logging
from typing import TypeVar, Optional, Any
from pydantic import BaseModel
from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


DataT = TypeVar("DataT")
logger = logging.getLogger("api")


class ErrorMessage(BaseModel):
    es: str
    en: str


class ErrorResponse(BaseModel):
    internal: Optional[Any]
    message: ErrorMessage
    status_code: int
    headers: Optional[dict]

    def log_error(
        self,
        exception: Exception = None,
        validation_error: RequestValidationError = None,
    ):
        msg = self.message.en
        if exception is not None:
            msg = f"{msg}: {exception}"
        if validation_error is not None:
            msg = f"{msg}: {validation_error.__str__}"
        logger.error(msg)

    def send(self, validation_error: RequestValidationError = None):
        self.log_error(validation_error)
        if validation_error is not None:
            self.internal = validation_error.errors()
        return JSONResponse(
            status_code=self.status_code,
            content=jsonable_encoder({"detail": self.dict()}),
        )

    def raise_exception(self, exception: Exception = None):
        self.log_error(exception)
        if exception is not None:
            self.internal = exception.args
        raise HTTPException(status_code=self.status_code, detail=self.dict(), headers=self.headers)

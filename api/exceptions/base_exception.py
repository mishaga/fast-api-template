from fastapi import HTTPException


class BaseApiException(HTTPException):
    """Base class for API exceptions."""

    status_code: int
    detail: str | None = None

    def __init__(self):
        """Init method."""
        super().__init__(status_code=self.status_code, detail=self.detail)

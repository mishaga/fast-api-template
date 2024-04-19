from pydantic import BaseModel


class HomeResponse(BaseModel):
    """Response for home page."""

    service: str
    version: str
    environment: str

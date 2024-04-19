from pydantic import BaseModel


class HealthPage(BaseModel):
    """Health page response."""

    database: bool

from pydantic import BaseModel


class Message(BaseModel):
    """Simple response with message only."""

    message: str

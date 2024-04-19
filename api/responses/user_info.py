from pydantic import BaseModel, PositiveInt


class UserInfo(BaseModel):
    """Response for user info page."""

    id: PositiveInt
    name: str

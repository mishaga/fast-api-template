import dataclasses


@dataclasses.dataclass(frozen=True)
class AuthUrlData:
    """AuthUrlData class for tests.

    Defines method and url.
    """

    method: str
    url: str

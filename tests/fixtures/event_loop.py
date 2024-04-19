import asyncio

import pytest

from tests.const import SCOPE_SESSION


@pytest.fixture(scope=SCOPE_SESSION)
def event_loop():
    """Event loop fixture.

    Creates one event loop for whole session of tests.
    """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

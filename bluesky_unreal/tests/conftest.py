import pytest
from bluesky_unreal.tests.api import test_api

@pytest.fixture(scope="session")
def api_fixture():
    with test_api():
        yield

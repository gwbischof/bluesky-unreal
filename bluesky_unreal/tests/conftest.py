import pytest
from bluesky_unreal.tests.api import test_api
from bluesky_unreal import UnrealClient

@pytest.fixture(scope="session")
def unreal_api():
    with test_api():
        yield

@pytest.fixture(scope="session")
def unreal_client():
    unreal_client = UnrealClient(server_address='http://localhost:8000')
    yield unreal_client

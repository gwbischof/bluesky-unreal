import asyncio
import pytest
import sys
import time

from bluesky_unreal import UnrealClient


def test_api_presets(api_fixture):
    client = UnrealClient(server_address='http://localhost:8000')
    print(client.get_presets())


def test_api_all_propertie(api_fixture):
    client = UnrealClient(server_address='http://localhost:8000')
    print(client.get_all_properties())


def test_api_get_value(api_fixture):
    client = UnrealClient(server_address='http://localhost:8000')
    assert 1 == client.get_value('dcm.bragg')


def test_api_set_value(api_fixture):
    client = UnrealClient(server_address='http://localhost:8000')
    client.set_value('dcm.bragg', 2)

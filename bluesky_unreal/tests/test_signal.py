import pytest

from bluesky_unreal import UnrealSignal

TEST_SERVER='http://localhost:8000'

def test_signal(unreal_api):
    signal = UnrealSignal('dcm.bragg', server=TEST_SERVER)



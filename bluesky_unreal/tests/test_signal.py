import pytest


def test_api_presets(unreal_api, unreal_client):
    print(unreal_client.get_presets())


def test_api_all_propertie(unreal_api, unreal_client):
    print(unreal_client.get_all_properties())


def test_api_get_value(unreal_api, unreal_client):
    assert 1 == unreal_client.get_value('dcm.bragg')


def test_api_set_value(unreal_api, unreal_client):
    unreal_client.set_value('dcm.bragg', 2)

import requests
import json


class UnrealClient():
    """
    Client for Unreal Engine Remote Control API.

    Parameters
    ----------
    server_address: string, optional
        The address of the Unreal Remote Control http server.
        Defaults to the Unreal Remote Control Plugin's default host and port.
    """

    def __init__(self, server_address='http://localhost:30010'):
        self.server_address = server_address

    def get_presets(self):
        result = requests.get(f'{self.server_address}/remote/presets')
        result_dict = json.loads(result.content)
        return [preset['Name'] for preset in result_dict['Presets']]

    def get_properties(self, preset_name):
        result = requests.get(f'{self.server_address}/remote/preset/{preset_name}')
        properties = json.loads(result.content)['Preset']['Groups'][0]['ExposedProperties']
        return [prop['DisplayName'] for prop in properties]

    def get_functions(self):
        result = requests.get(f'{self.server_address}/remote/assets')
        return json.loads(result.content)

    def get_all_properties(self):
        presets = self.get_presets()
        exposed_properties = {preset_name: self.get_properties(preset_name) for preset_name in presets}
        return exposed_properties

    def get_value(self, name):
        print("GET_VALUE", name)
        if len(name.split('.')) != 2:
            raise ValueError("GET_VALUE", f"Name must contain a '.' preset_name.property_name, name={name}")
        preset_name = name.split('.')[0]
        property_name = name.split('.')[1]
        result = requests.get(f'{self.server_address}/remote/preset/{preset_name}/property/{property_name}')
        value = json.loads(result.content)['PropertyValues'][0]['PropertyValue']
        return value

    def set_value(self, name, value):
        HEADERS = {'Content-type': 'application/json'}
        if len(name.split('.')) != 2:
            raise ValueError("SET_VALUE", f"Name must contain a '.' preset_name.property_name, name={name}")
        preset_name = name.split('.')[0]
        property_name = name.split('.')[1]
        result = requests.put(f'{self.server_address}/remote/preset/{preset_name}/property/{property_name}',
                              headers=HEADERS,
                              data=json.dumps({"PropertyValue": value,
                                               "GenerateTransaction": 1}))
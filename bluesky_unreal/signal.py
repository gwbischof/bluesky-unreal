from ophyd import Component as Cpt
from ophyd import Device, Signal
from ophyd.sim import NullStatus

from bluesky_unreal import UnrealClient

class UnrealSignal(Signal):
    """
    Ophyd Signal to interface with Unreal Engine.

    Parameters
    ----------
    preset_name: string
        The name of the Unreal Remote Control Preset.
        A Preset is like a group of Properties.
    name: string
        The name of the Unreal property
    server_address: string, optional
        The address of the Unreal Remote Control http server
        Defaults to the Unreal Remote Control Plugin's default host and port.
    """

    def __init__(self, *args, preset_name, server_address='http://localhost:30010', **kwargs):
        super().__init__(*args, **kwargs)
        self._client = UnrealClient(server_address)
        self._preset_name = preset_name

    def set(self, value, *arg, **kwargs):
        self._readback = value
        self._client.set_value(self._preset_name, self.name, value)
        return NullStatus()

    def get(self, **kwargs):
        return self._client.get_value(self._preset_name, self.name)

    def put(self, *args, **kwargs):
        self.set(*args, **kwargs).wait()

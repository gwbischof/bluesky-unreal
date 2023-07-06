from ophyd import Component as Cpt
from ophyd import Device, Signal
from ophyd.sim import NullStatus

from bluesky_unreal import UnrealClient

class UnrealSignal(Signal):
    """
    Ophyd Signal to interface with Unreal Engine.

    Parameters
    ----------
    name: string
        The name of the Unreal property
    server_address: string, optional
        The address of the Unreal Remote Control http server
        Defaults to the Unreal Remote Control Plugin's default host and port.
    """

    def __init__(self, name, **kwargs):
        server_address='http://localhost:30010'

        metadata = {}
        kwargs.setdefault("value", 0)

        super().__init__(name=name, metadata=metadata, **kwargs)
        self._client = UnrealClient(server_address)

    def set(self, value, *args, **kwargs):
        self._readback = value
        self._client.set_value(f"{self.name}", value)
        return NullStatus()

    def get(self, **kwargs):
        return self._client.get_value(f"{self.name}")

    def put(self, *args, **kwargs):
        self.set(*args, **kwargs).wait()

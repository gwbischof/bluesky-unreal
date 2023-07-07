from ophyd import Signal
from ophyd.sim import NullStatus

from bluesky_unreal import UnrealClient


class UnrealSignal(Signal):
    """
    Ophyd Signal to interface with Unreal Engine.

    Parameters
    ----------
    name: string
        The name of the Unreal property
    server: string, optional
        The address of the Unreal Remote Control http server
        Defaults to the Unreal Remote Control Plugin's default host and port.
    """

    def __init__(self, variable_name, *, name=None, server='http://localhost:30010', **kwargs):
        kwargs.setdefault("value", 0)
        self._client = UnrealClient(server)
        name = variable_name
        print("NAME", name, "PVNAME", variable_name)
        super().__init__(name=name, **kwargs)

    def set(self, value, *args, **kwargs):
        self._readback = value
        self._client.set_value(f"{self.name}", value)
        return NullStatus()

    def get(self, **kwargs):
        return self._client.get_value(f"{self.name}")

    def put(self, *args, **kwargs):
        self.set(*args, **kwargs).wait()

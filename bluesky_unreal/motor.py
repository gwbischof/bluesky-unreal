from ophyd import FormattedComponent, Device
from ophyd.positioner import SoftPositioner
from bluesky_unreal import UnrealClient, UnrealSignal

TEST_SERVER='http://localhost:8000'


class UnrealMotor(Device, SoftPositioner):
    """
    An Unreal Engine ophyd motor which tries to mimic some of the functionality of EpicsMotor.

    Parameters
    ----------
    variable_name: string
        The name of the Unreal property
    server: string, optional
        The address of the Unreal Remote Control http server
        Defaults to the Unreal Remote Control Plugin's default host and port.
    name: None
        Don't pass a name, its gets overwitten by variable_name.
        This is a hack to make this work, this idea is from EpicsSignalBa
    """

    # FormattedComponent doesn't prefix the parent name.
    user_readback = FormattedComponent(UnrealSignal, '{self.name}', server=TEST_SERVER)
    user_setpoint = FormattedComponent(UnrealSignal, '{self.name}', server=TEST_SERVER)

    def __init__(self, variable_name, *, name=None, server='http://localhost:30010', **kwargs):
        name=variable_name
        self.server = server
        super().__init__(name=name, **kwargs)
        self._client = UnrealClient(server)

        try:
            init_pos = self._client.get_value(f"{self.name}")
            self._position= init_pos
        except Exception:
            pass

    def _setup_move(self, position, status):
         self._client.set_value(f"{self.name}", position)
         super()._setup_move(position, status)

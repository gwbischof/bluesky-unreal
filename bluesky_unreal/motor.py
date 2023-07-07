from ophyd import FormattedComponent, Device
from ophyd.positioner import SoftPositioner
from bluesky_unreal import UnrealClient, UnrealSignal

TEST_SERVER='http://localhost:8000'


class UnrealMotor(Device, SoftPositioner):
    """
    An Unreal Engine ophyd motor which tries to mimic some of the functionality of EpicsMotor.
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

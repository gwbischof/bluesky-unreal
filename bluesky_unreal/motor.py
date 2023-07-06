from ophyd import FormattedComponent, Device
from ophyd.positioner import SoftPositioner
from bluesky_unreal import UnrealClient, UnrealSignal

class UnrealMotor(Device, SoftPositioner):
    """
    An Unreal Engine ophyd motor which tries to mimic some of the functionality of EpicsMotor.
    """

    # FormattedComponent doesn't prefix the parent name.
    user_readback = FormattedComponent(UnrealSignal, 'dcm.bragg')
    user_setpoint = FormattedComponent(UnrealSignal, 'dcm.bragg')

    def __init__(self, prefix, **kwargs):
        super().__init__(prefix, **kwargs)
        server_address='http://localhost:30010'
        self._client = UnrealClient(server_address)
        self.user_readback.name = prefix
        self.user_setpoint.name = prefix
        print("NAME", self.name, "PREFIX", self.prefix)
        try:
            init_pos = self._client.get_value(f"{self.name}")
            self._position= init_pos
        except Exception:
            pass

    def _setup_move(self, position, status):
         self._client.set_value(f"{self.name}", position)
         super()._setup_move(position, status)
from ophyd import FormattedComponent, Device
from ophyd.positioner import SoftPositioner
from ophyd.sim import SynSignal
from bluesky_unreal import UnrealClient, UnrealSignal


#SERVER='http://localhost:8000'
SERVER='http://localhost:30010'


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
    user_readback = FormattedComponent(UnrealSignal, '{self.name}', server=SERVER, kind='normal')
    user_setpoint = FormattedComponent(UnrealSignal, '{self.name}', server=SERVER, kind='normal')
    user_offset = FormattedComponent(SynSignal, func=lambda: 1, kind='normal')

    def __init__(self, variable_name, *, name=None, server='http://localhost:30010', **kwargs):
        name=variable_name
        self.server = server
        self._client = UnrealClient(server)
        init_pos = self._client.get_value(f"{name}")
        super().__init__(name=name, init_pos=init_pos, **kwargs)

    def _setup_move(self, position, status):
         self._client.set_value(f"{self.name}", position)
         super()._setup_move(position, status)

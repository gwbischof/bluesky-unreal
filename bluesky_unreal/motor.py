from ophyd import FormattedComponent, Device, Signal
from ophyd.positioner import SoftPositioner
from ophyd.sim import SynSignal
from bluesky_unreal import UnrealClient, UnrealSignal


#SERVER='http://localhost:8000'
SERVER='http://localhost:30010'


class EnumSignal(Signal):
    def enum_strs(self):
        return ("Off","On")
    

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
    user_readback = FormattedComponent(UnrealSignal, '{self.variable_name}', server=SERVER, kind='normal')
    user_setpoint = FormattedComponent(UnrealSignal, '{self.variable_name}', server=SERVER, kind='normal')
    user_offset = FormattedComponent(SynSignal, func=lambda: 1., kind='config')
    velocity = FormattedComponent(Signal, value=1., kind='config')
    hocpl = FormattedComponent(Signal, value= 1., kind='config')
    amfe =  FormattedComponent(EnumSignal, value= 0, kind='config')
    amfae =  FormattedComponent(EnumSignal, value= 0, kind='config')


    def __init__(self, variable_name, *, name=None, server='http://localhost:30010', **kwargs):
        #name=variable_name
        self.variable_name = variable_name
        self.server = server
        self._client = UnrealClient(server)
        init_pos = self._client.get_value(variable_name)
        super().__init__(name=name, init_pos=init_pos, **kwargs)

    def _setup_move(self, position, status):
         self._client.set_value(f"{self.variable_name}", position)
         super()._setup_move(position, status)


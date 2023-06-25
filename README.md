# bluesky-unreal
Control unreal simulations with bluesky.

---

## Example


This example requires the Unreal Robot Arm Simulation
found here: https://github.com/gwbischof/robot_arm

### List all of the exposed Unreal properties.
```
from unreal_remote_control import UnrealClient, UnrealSignal
client = UnrealClient()
client.get_all_properties()
```

### Create Ophyd signals for the properties that we want to access.
```
motor1 = UnrealSignal(preset_name="NewRemoteControlPreset", name='motor1')
motor2 = UnrealSignal(preset_name="NewRemoteControlPreset", name='motor2')
motor3 = UnrealSignal(preset_name="NewRemoteControlPreset", name='motor3')
motor4 = UnrealSignal(preset_name="NewRemoteControlPreset", name='motor4')
```

### Run a grid scan with the Robot Arm.
```
from bluesky import RunEngine
from bluesky.plans import grid_scan
RE = RunEngine({})
RE(grid_scan([], motor1, 0, 50, 10, motor2, 0, 50, 10, motor3, -20, 20, 10, snake_axes=True))
```

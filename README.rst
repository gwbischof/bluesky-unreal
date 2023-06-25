==============
bluesky-unreal
==============

.. image:: https://github.com/gwbischof/bluesky-unreal/actions/workflows/testing.yml/badge.svg
   :target: https://github.com/gwbischof/bluesky-unreal/actions/workflows/testing.yml


.. image:: https://img.shields.io/pypi/v/bluesky-unreal.svg
        :target: https://pypi.python.org/pypi/bluesky-unreal


control unreal simulations with bluesky

* Free software: 3-clause BSD license
* Documentation: (COMING SOON!) https://gwbischof.github.io/bluesky-unreal.

This requires the Unreal Robot Arm Simulation.
And the code here: https://gist.github.com/gwbischof/32c2de9e8e5521752d442cef3365d9b4

## List all of the exposed Unreal properties.
```
from unreal_remote_control import UnrealClient, UnrealSignal
client = UnrealClient()
client.get_all_properties()
```

## Create Ophyd signals for the properties that we want to access.
```
motor1 = UnrealSignal(preset_name="NewRemoteControlPreset", name='motor1')
motor2 = UnrealSignal(preset_name="NewRemoteControlPreset", name='motor2')
motor3 = UnrealSignal(preset_name="NewRemoteControlPreset", name='motor3')
motor4 = UnrealSignal(preset_name="NewRemoteControlPreset", name='motor4')
```

## Run a grid scan with the Robot Arm.
```
from bluesky import RunEngine
from bluesky.plans import grid_scan
RE = RunEngine({})
RE(grid_scan([], motor1, 0, 50, 10, motor2, 0, 50, 10, motor3, -20, 20, 10, snake_axes=True))
```

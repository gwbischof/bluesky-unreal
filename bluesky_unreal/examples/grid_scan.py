"""
This example shows how we can run bluesky scans on an robot arm in Unreal Engine 5.
The robot arm project can be found here: https://github.com/gwbischof/robot_arm

The robot_arm project uses the remote control api plugin for unreal engine, the
project exposes the robot arm motor positions so that we can manipulat the robot arm
over a network.
"""

from bluesky import RunEngine
from bluesky.plans import grid_scan
from bluesky_unreal import UnrealClient, UnrealSignal

# List all of the exposed Unreal properties.
client = UnrealClient()
client.get_all_properties()

# Create UnrealSignals for the properties that we want to access.
motor1 = UnrealSignal(preset_name="NewRemoteControlPreset", name='motor1')
motor2 = UnrealSignal(preset_name="NewRemoteControlPreset", name='motor2')
motor3 = UnrealSignal(preset_name="NewRemoteControlPreset", name='motor3')
motor4 = UnrealSignal(preset_name="NewRemoteControlPreset", name='motor4')

# Run a grid scan with the Robot Arm.
RE = RunEngine({})
RE(grid_scan([], motor1, 0, 50, 10, motor2, 0, 50, 10, motor3, -20, 20, 10, snake_axes=True))

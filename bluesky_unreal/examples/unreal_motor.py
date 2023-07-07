"""
How to use an UnrealSignal.

tests/api.py can be used to simulate the unreal remote control api.
TODO: Change this to markdown.
"""

from bluesky import RunEngine
from bluesky_unreal import UnrealMotor

TEST_SERVER = "http://localhost:8000"

# Create a motor.
motor = UnrealMotor("dcm:bragg", server=TEST_SERVER)


## Use the device in a plan.
# RE = RunEngine()
# RE.subscribe(print)
# RE(count([device1.bragg], num=3, delay=1))

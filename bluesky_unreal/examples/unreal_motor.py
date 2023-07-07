"""
How to use an UnrealSignal.

tests/api.py can be used to simulate the unreal remote control api.
TODO: Change this to markdown.
"""

from bluesky import RunEngine
from bluesky.plans import count
from bluesky_unreal import UnrealMotor

SERVER = "http://localhost:8000"


# Create a motor.
motor = UnrealMotor("dcm:bragg", server=SERVER)
motor.move(20)

## Use the device in a plan.
RE = RunEngine()
RE.subscribe(print)
RE(count([motor], num=3, delay=1))

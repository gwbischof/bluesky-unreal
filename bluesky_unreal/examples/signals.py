"""
Trying some different things with the unreal signal.

tests/api.py can be used to simulate the unreal remote control api.
"""
from bluesky import RunEngine
from bluesky.plans import count
from ophyd import Device, Component, FormattedComponent
from bluesky_unreal import UnrealSignal
TEST_SERVER='http://localhost:8000'

# Signals require a name if they are not a component.
signal = UnrealSignal('dcm.bragg', server=TEST_SERVER)

# Get a dictionary of information about the signal.
print("signal.read()", signal.read())

# Get the value.
print("signal.get()", signal.get())

class A(Device):

    # When a signal is a component you dont pass a name.
    # The second argument of a Component is the Suffix.
    # Extra Component kwargs are passed to the Signal init.

    # None of these behave the way that I would expect.
    #signal1 = Component(UnrealSignal, 'signal1_arg')
    signal2 = FormattedComponent(UnrealSignal, 'dcm.bragg', server=TEST_SERVER)
    #signal3 = Component(UnrealSignal, name='signal3_arg')
    #signal4 = FormattedComponent(UnrealSignal, name='signal4_arg')


a = A(name='a')

print("Signals", a._signals)


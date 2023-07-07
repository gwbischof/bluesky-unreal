
#Run bsui first
from bluesky.plans import scan
from bluesky import RunEngine
from ophyd.sim import det


RE = RunEngine()
RE(scan([det],dcm,4000,23000,20))
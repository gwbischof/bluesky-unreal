from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

from bluesky_unreal.client import UnrealClient
from bluesky_unreal.signal import UnrealSignal

"""
This api simulates the Unreal RemoteControl API.
"""

import contextlib
import subprocess
import sys
import time
import uvicorn
from typing import Union, Any
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/remote/presets")
async def presets():
    return {"Presets": [{"Name": "dcm"}]}


@app.get("/remote/preset/{preset_name}")
async def properties(preset_name: str):
    properties = {
        "Preset": {
            "Groups": [
                {"ExposedProperties": [{"DisplayName": "bragg"}, {"DisplayName": "para"}, {"DisplayName": "perp"}]}
            ]
        }
    }
    return properties


@app.get("/remote/preset/{preset_name}/property/{property_name}")
async def get_value(preset_name: str, property_name: str):
    properties = {
        'bragg':
        {"PropertyValues": [{'PropertyValue': 1}]},
        'para':
        {"PropertyValues": [{'PropertyValue': 2}]},
        'perp':
        {"PropertyValues": [{'PropertyValue': 3}]},
    }
    return properties.get(property_name, [])


@app.post("/remote/preset/{preset_name}/property/{property_name}")
async def set_value(preset_name: str, property_name: str, item: Any):
    print(item)
    return item


def main():
    uvicorn.run(app, host="127.0.0.1", port=8000)


@contextlib.contextmanager
def test_api():
    try:
        ps = subprocess.Popen(
            [
                sys.executable,
                "-c",
                f"from bluesky_unreal.tests.api import main; main()",
            ]
        )
        time.sleep(3)
        yield ps
    finally:
        ps.terminate()


if __name__ == "__main__":
    main()

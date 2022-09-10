import logging
import glob
import sys
import asyncio
import importlib

from PokeTide import app
from pyrogram import idle
from pathlib import Path

def load_plugins(plugin_name):
    root = "PokeTide/plugins/*.py"
    total = f"{len(glob.glob(root))}"
    path = Path(f"PokeTide/plugins/{plugin_name}.py")
    name = "PokeTide.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["PokeTide.plugins." + plugin_name] = load
    print("Total Plugins -->" + total)
    print("Imported --> " + plugin_name)

path = "PokeTide/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        thepath = Path(a.name)
        plugin_name = thepath.stem
        load_plugins(plugin_name.replace(".py", ""))
 
if __name__ == "__main__":
 print("Successfully Started")
 print("Project By Aasfcyberking For PokeTideBots")
 idle()

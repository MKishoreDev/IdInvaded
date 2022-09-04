import logging
import glob
import sys
import time
import asyncio
import importlib
import datetime

from Invaded import inv, log, BOT_NAME, UBOT_NAME, LOG_GROUP_ID
from pyrogram import idle, __version__
from pathlib import Path

now = datetime.datetime.now()
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
ts = datetime.datetime.timestamp(now)
boot_msg = f"""Started Your Invaded Successfully...
Day: %s
Time: {current_time}
Client: {BOT_NAME}
Scanner: {UBOT_NAME}
Pyrogram: {__version__}
Timestamp: {ts}"""

FORMAT = "[INFO] %(message)s"

def load_plugins(plugin_name):
    root = "Invaded/plugins/*.py"
    total = f"{len(glob.glob(root))}"
    path = Path(f"Invaded/plugins/{plugin_name}.py")
    name = "Invaded.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["Invaded.plugins." + plugin_name] = load
    print("Total Plugins -->" + toral)
    print("Imported --> " + plugin_name)

path = "Invaded/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        thepath = Path(a.name)
        plugin_name = thepath.stem
        names = plugin_name.replace(".py", "")
        load_plugins(names)

async def main():
 logging.basicConfig(
     handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
     level=logging.INFO,
     format=FORMAT,
     datefmt="[%X]",
  )
 log.info(sys.version + "\n\n" +  (boot_msg % (now.strftime("%A"))))
 logging.getLogger("pyrogram").setLevel(logging.INFO)
 log.info("Project By AuraMoon55 | Ryu120 | AasfCyberKing")
 
if __name__ == "__main__":
    asyncio.run(main())
    idle()

import logging
import sys
import time
import importlib
import datetime

from Invaded import inv, log
from Invaded.plugins import ALL_MODULES
from pyrogram import idle, __version__

now = datetime.datetime.now()
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
ts = datetime.datetime.timestamp(now)
boot_msg = f"""Started Your Invaded Successfully...
Day: %s
Time: {current_time}
Pyrogram: {__version__}
Timestamp: {ts}"""

FORMAT = "[INFO] %(message)s"

if __name__ == "__main__":
    logging.basicConfig(
        handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
        level=logging.INFO,
        format=FORMAT,
        datefmt="[%X]",
    )
    log.info(sys.version + "\n\n" +  (boot_msg % (now.strftime("%A"))))
    logging.getLogger("pyrogram").setLevel(logging.INFO)
    for module in ALL_MODULES:
      importlib.import_module("Invaded.plugins." + module)
    
    print("Project By AuraMoon55 | Ryu120 | AasfCyberKing")
 #   inv.send(LOG_GROUP_ID, "I Am Online")
    idle()

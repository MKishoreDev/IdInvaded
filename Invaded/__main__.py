import logging
import sys
import importlib
import datatime

from Invaded import inv, log
from Invaded.plugins import ALL_MODULES
from pyrogram import idle

now = datetime.datetime.now()
boot_msg = """Started Your Invaded Successfully...
Day: %s"""

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

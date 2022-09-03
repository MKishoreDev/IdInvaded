import logging
import sys
import time
import asyncio
import importlib
import datetime

from Invaded import inv, log, BOT_NAME, UBOT_NAME
from Invaded.plugins import ALL_MODULES
from pyrogram import idle, __version__

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

async def main():
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
   log.info("Successfully Imported Plugins:" + module)
 log.info("Project By AuraMoon55 | Ryu120 | AasfCyberKing")
 await inv.send_video(LOG_GROUP_ID, "https://telegra.ph/file/a69feed5d48f6554ac47a.mp4", caption="**Invaded Started Successfully**\n\n`Invaders!!! Let's Defeat The Darkness`")

if __name__ == "__main__":
    asyncio.run(main())
    idle()

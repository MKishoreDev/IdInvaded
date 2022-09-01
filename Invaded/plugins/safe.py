import os
import sys
import subprocess

from Invaded import inv, invaded_cmd, GODS
from pyrogram import filters

@inv.on_message(invaded_cmd("gitpull") & filters.user(GODS))
async def gitpull(_, message):
    subprocess.Popen("git pull", stdout=subprocess.PIPE, shell=True)
    await message.reply_text("`Git Pulled Probably`")
    os.system("restart.bat")
    os.execv("start.bat", sys.argv)


@inv.on_message(invaded_cmd("restart") & filters.user(GODS))
async def restart(_, message):
    await message.reply_text("`Restarting...`")
    await inv.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    sys.exit()


@inv.on_message(invaded_cmd("shutdown") & filters.user(GODS))
async def shutdown(event):
    await message.reply_text("`Shutting Down...`")
    await imv.disconnect()

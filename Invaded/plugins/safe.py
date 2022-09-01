import os
import sys
import subprocess

from Invaded import inv, invaded_cmd, GODS
from pyrogram import filters

__module__ = "Safe"
__help__ = """
• `/gitpull` - `To Git Pulled` `[Developer Restricted]`
• `/restart` - `To Restart The Client` `[Developer Restricted]`
• `/shutdown` - `To Shutdown The Client` `[Developer Restricted]`
**Note:- All Commands Given Bellow Can Be Used With** `inv`, `Inv`, `invaded`, `Invaded`, `?`, `$`, `!`, `.`, or `/`
"""

@inv.on_message(invaded_cmd("gitpull") & filters.user(GODS) & ~filters.forwarded)
async def gitpull(_, message):
    subprocess.Popen("git pull", stdout=subprocess.PIPE, shell=True)
    await message.reply_text("`Git Pulled Probably`")
    os.system("restart.bat")
    os.execv("start.bat", sys.argv)


@inv.on_message(invaded_cmd(['restart','reboot']) & filters.user(GODS) & ~filters.forwarded)
async def restart(_, message):
    await message.reply_text("`Restarting...`")
    await inv.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    sys.exit()


@inv.on_message(invaded_cmd("shutdown") & filters.user(GODS) & ~filters.forwarded)
async def shutdown(event):
    await message.reply_text("`Shutting Down...`")
    await imv.disconnect()

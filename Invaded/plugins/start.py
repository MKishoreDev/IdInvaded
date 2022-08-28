import time
import asyncio
import re
import datetime
import random
import requests

from Invaded import inv, invaded_cmd, StartTime
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import filters, enums

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


buttons = [
    [
        InlineKeyboardButton(
            text=f"✲ Summon Me ✲", url=f"telegram.me/Kawaii_Robot?startgroup=true")
    ],
    [
        InlineKeyboardButton(text="[► Report Error ◄]", url="https://t.me/Aasf_Cyberking"),
        InlineKeyboardButton(text="[► Get Updates ◄]", url="https://t.me/CityOfCreations"),
    ],
    [
        InlineKeyboardButton(text="⊵ Help Guidelines ⊴", callback_data="help_enter"),
    ],
]


PM_START_TEXT = """
`Hello There I Am` `I⊃：INVΛ⊃≡⊃` `The Judgement Enforcing System`

**Invaded Analysis Report :-**
 ➛ **User:** {}
 ➛ **ID:** `{}`
 ➛ **Is Restricted:** `No`
 ➛ **Status:** `Civilian`
 ➛ **Crime Coefficient:** `Under - 100`
"""

GROUP_START_TEXT = """
`Hello There I Am` `I⊃：INVΛ⊃≡⊃` `The Judgement Enforcing System`

**Invaded Analysis Report :-**
 ➛ **Group:** {}
 ➛ **ID:** `{}`
 ➛ **Members Count:** `{}`
 ➛ **Admins Count:** `{}`
 ➛ **Bots Count:** `{}`
 ➛ **Message Count:** `{}`
"""

@inv.on_message(invaded_cmd("start"))
async def test(_, m: Message):
    if m.chat.type == enums.ChatType.PRIVATE:
        uptime = get_readable_time((time.time() - StartTime))
        kk = await m.reply(text="`Analyzing The User`")
        asyncio.sleep(2)
        mm = await kk.edit_text("`...`")
        asyncio.sleep(2)
        ll = await mm.edit_text("`Processing...`")
        asyncio.sleep(3)
        await ll.delete()
        await m.reply_photo(
            "https://telegra.ph/file/e9a7b101e8fcc7e6b7381.jpg",
            caption=PM_START_TEXT.format(
                m.from_user.mention, m.from_user.id
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if not m.chat.type == enums.ChatType.PRIVATE:
        uptime = get_readable_time((time.time() - StartTime))
        count = await inv.get_chat_members_count(m.chat.id)
        admins = await inv.get_chat_members(m.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        bots = await inv.get_chat_members(m.chat.id, filter=enums.ChatMembersFilter.BOTS)
        msgc = await inv.search_messages_count(m.chat.id)
        kk = await m.reply(text="`Analyzing The User...`")
        asyncio.sleep(2)
        await kk.delete()
        await m.reply_photo(
            "https://telegra.ph/file/83b667369505a14c8fef2.jpg",
            caption=GROUP_START_TEXT.format(
                m.chat.mention,
                m.chat.id,
                count,
                admins
                bots,
                msgc
                reply_markup=InlineKeyboardMarkup(buttons),
            ),
        )

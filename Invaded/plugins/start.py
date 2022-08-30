import asyncio

from Invaded import inv, invaded_cmd
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import filters, enums

buttons = [
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
 ➛ **Group:** `{}`
 ➛ **ID:** `{}`
 ➛ **Members Count:** `{}`
 ➛ **Admins Count:** `{}`
 ➛ **Bots Count:** `{}`
 ➛ **Message Count:** `{}`
"""

@inv.on_message(invaded_cmd("start"))
async def test(_, m: Message):
    if m.chat.type == enums.ChatType.PRIVATE:
        kk = await m.reply(text="`Analyzing The User`")
        await asyncio.sleep(2)
        mm = await kk.edit_text("`...`")
        await asyncio.sleep(2)
        ll = await mm.edit_text("`Processing...`")
        await asyncio.sleep(3)
        await ll.delete()
        await m.reply_photo(
            "https://telegra.ph/file/e9a7b101e8fcc7e6b7381.jpg",
            caption=PM_START_TEXT.format(
                m.from_user.mention, m.from_user.id
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if not m.chat.type == enums.ChatType.PRIVATE:
     try:
        kk = await m.reply(text="`Analyzing The User...`")
        await asyncio.sleep(2)
        await kk.delete()
        count = await inv.get_chat_members_count(m.chat.id)
        admins = inv.get_chat_members(m.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)
        bots = inv.get_chat_members(m.chat.id, filter=enums.ChatMembersFilter.BOTS)
        msgc = await inv.search_messages_count(m.chat.id)
        await m.reply_photo(
            "https://telegra.ph/file/83b667369505a14c8fef2.jpg",
            caption=GROUP_START_TEXT.format(
                m.chat.title,
                m.chat.id,
                count,
                admins,
                bots,
                msgc),
                reply_markup=InlineKeyboardMarkup(buttons)
        )
     except Exception as e:
         await m.reply_photo("https://c4.wallpaperflare.com/wallpaper/976/117/318/anime-girls-404-not-found-glowing-eyes-girls-frontline-wallpaper-preview.jpg", caption=f"`404 Error Occurred Failed To Start The Invaded`\n\n `{e}`")
         return

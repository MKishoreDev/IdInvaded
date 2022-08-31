from Invaded import inv, invaded_cmd, BOT_NAME
from Invaded.plugins.start import PM_START_TEXT, PM_PHOTO, PM_KEYBOARD
from Invaded.utils.misc import paginate_modules
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
import re

PM_STRING = """
**Hey Wanna Know My Commands ?**

`Check It Out By Clicking The Given Button Bellow ^_^`
"""
async def help_parser(name, keyboard=None):
  if not keyboard:
    keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    return ("""
**Hello,** {} `Check My Commands By Clicking The Buttons Give Bellow`
`I Am {} I Have Lot's Of Features That Makes You Feel Safety On Telegram`
**Note:- All Commands Given Bellow Can Be Used With** `inv`, `Inv`, `invaded`, `Invaded`, `?`, `$`, `!`, `.`, or `/`
""".format(name, BOT_NAME), keyboard)



@inv.on_message(invaded_cmd("help"))
async def _help(_, message):
if message.chat.type == enums.ChatType.PRIVATE:
  text, keyboard = await help_parser(message.from_user.mention)
  return await message.reply_photo(
      photo="https://telegra.ph/file/90a0be7175ad57fcaa21e.jpg",
      caption=text,
      reply_markup=keyboard
    )
else:
    await inv.send_photo(message.chat.id , "https://telegra.ph/file/cd1611c22cc9ad650e0de.jpg" ,  caption=PM_STRING , reply_markup=InlineKeyboardMarkup(
       [
           [InlineKeyboardButton("Click Here To Explore" , url="t.me/Invaded_Robot?start=help")]            
       ]))



@inv.on_callback_query(filters.regex("inv_commands"))
async def commands_callbacc(_, query):
  text, keyboard = await help_parser(query.from_user.mention)
  await query.message.edit_media(
    media=InputMediaPhoto(
      "https://telegra.ph/file/90a0be7175ad57fcaa21e.jpg",
      caption=text
    ),
    reply_markup=keyboard
  )
  return await inv.answer_callback_query(query.id)

@inv.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(client, query):
  home_match = re.match(r"help_home\((.+?)\)", query.data)
  mod_match = re.match(r"help_module\((.+?)\)", query.data)
  create_match = re.match(r"help_create", query.data)
  top_text = """
**Hello,** {} `Check My Commands By Clicking The Buttons Give Bellow`
`I Am {} I Have Lot's Of Features That Makes You Feel Safety On Telegram`
**Note:- All Commands Given Bellow Can Be Used With** `inv`, `Inv`, `invaded`, `Invaded`, `?`, `$`, `!`, `.`, or `/`
""".format(query.from_user.first_name, BOT_NAME)
  if mod_match:
    module = (mod_match.group(1)).replace(" ", "_")
    text = (
        "**{}** `{}`:\n".format(
          "Here Is The Help For The", HELPABLE[module].__MODULE__
        )
        + HELPABLE[module].__HELP__
    )

    await query.message.edit_caption(
      caption=text,
      reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("back", callback_data="help_back")]]
      )
    )

  elif home_match:
    await query.message.edit_media(
      media=InputMediaPhoto(PM_PHOTO, caption=PM_START_TEXT),
      reply_markup=PM_KEYBOARD
    )

  elif create_match:
    text, keyboard = await help_parser(query.from_user.first_name)
    await query.message.edit_caption(
      caption=text,
      reply_markup=keyboard
    )

  return await inv.answer_callback_query(query.id)

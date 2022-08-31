from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Invaded import inv, inv_modules, invaded_cmd
from typing import List , Any

HELP_STRING = """
Hey, see my commands down
Report issues @idk
"""
PM_STRING = """
**Hey Wanna Know My Commands**
`Check It Out By Clicking The Given Button Bellow`
"""

@inv.on_message(invaded_cmd('help'))
def invhelp(_,message):
    if message.chat.type == enums.ChatType.PRIVATE:
        keyboard = []
        for x in inv_modules:
            keyboard.append([InlineKeyboardButton(f"{x['Module_Name']}" , callback_data=f"help:{x['Module_Name']}")])


        inv.send_message(message.chat.id , HELP_STRING , reply_markup=InlineKeyboardMarkup(keyboard))

    else:
        inv.send_photo(message.chat.id , "https://telegra.ph/file/cd1611c22cc9ad650e0de.jpg" ,  caption=PM_STRING , reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Click Here To Explore" , url="t.me/Invaded_Robot?start=help")]
            
            ]))

from pyrogram import filters, enums
from pyrogram.types import callback_data, InlineKeyboardButton, InlineKeyboardMarkup
from Invaded import inv, inv_modules, invaded_cmd
from typing import List , Any

HELP_STRING = """
Hey, see my commands down
Report issues @idk
"""

@inv.on_message(invaded_cmd('help'))
def invhelp(_,message):
    if message.chat.type == enums.ChatType.PRIVATE:
        keyboard = []
        for x in invaded_command:
            keyboard.append([InlineKeyboardButton(f"{x['Module_Name']}" , callback_data=f"help:{x['Module_Name']}")])


        inv.send_message(message.chat.id , HELP_STRING , reply_markup=InlineKeyboardMarkup(keyboard))

    else:
        inv.send_photo(message.chat.id , "https://telegra.ph/file/cd1611c22cc9ad650e0de.jpg" ,  caption=HELP_STRING , reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Pm me for more details"  , url="t.me/Invaded_Robot?start=help")]
            
            ]))

from pyrogram import filters
from pyrogram.types.bots_and_keyboards import callback_game
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup 
from Invaded import inv, inv_modules, invaded_command
from typing import List , Any

HELP_STRING = """
Hey, see my commands down
Report issues @idk
"""

@inv.on_message(invaded_command('help'))
def invhelp(_,message):
    if message.chat.type == "private":
        keyboard = []
        for x in invaded_command:
            keyboard.append([InlineKeyboardButton(f"{x['Module_Name']}" , callback_data=f"help:{x['Module_Name']}")])


        inv.send_message(message.chat.id , HELP_STRING , reply_markup=InlineKeyboardMarkup(keyboard))

    else:
        inv.send_photo(message.chat.id , "https://telegra.ph/file/cd1611c22cc9ad650e0de.jpg" ,  caption=HELP_STRING , reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Pm me for more details"  , url="t.me/Invaded_Robot?start=help")]
            
            ]))

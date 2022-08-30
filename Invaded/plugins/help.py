from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Invaded import inv, invaded_cmd
from typing import List , Any

HELP_STRING = """
Hey, see my commands down
Report issues @idk
"""

@inv.on_message(invaded_cmd('help'))
def invhelp(_,message):

        inv.send_photo(message.chat.id , "https://telegra.ph/file/cd1611c22cc9ad650e0de.jpg" ,  caption=HELP_STRING , reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Pm me for more details"  , url="t.me/Invaded_Robot?start=help")]
            
            ]))

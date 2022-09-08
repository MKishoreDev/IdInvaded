from Invaded import inv
from pyrogram import enums
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultAnimation,
)

@inv.on_inline_query()
async def inline_query_handler(client, query):
    string = query.query.lower()
    if string == "scanner_help":
        await client.answer_inline_query(
            query.id,
            results=[
                InlineQueryResultAnimation(
                    caption="""
**Hello There,** `Check My Commands By Clicking The Buttons Give Bellow`
`I Am I⊃：INVΛ⊃≡⊃ The Judgement Enforcing System I Have Lot's Of Features That Makes You Feel Safety On Telegram`
**Note:- All Commands Given Bellow Can Be Used With** `inv`, `Inv`, `invaded`, `Invaded`, `?`, `$`, `!`, `.`, or `/`""",
                    animation_url="https://telegra.ph/file/a69feed5d48f6554ac47a.mp4",
                    parse_mode=enums.ParseMode.MARKDOWN,
                    title="Checkout My Commands",
                    description="Click Here For Invaded's Detailed Help...",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="Dev", url="https://telegram.me/AASF_CYBERKING"
                                )
                            ]
                        ]
                    ),
                ),
            ],
            switch_pm_text="I⊃：INVΛ⊃≡⊃",
            switch_pm_parameter="start",
            cache_time=300,
        )

import asyncio

from pyrogram import Client 

APP_ID = input("\nEnter Your API_ID:\n > ")
APP_HASH = input("\nEnter Your API_HASH:\n >")

print("\nEnter Your Phone Number When Asked\n")

ubot = Client("__name__", api_id=APP_ID, api_hash=APP_HASH, in_memory=True)

async def main():
    await ubot.start()
    string = await ubot.export_session_string()
    info = await ubot.get_me()
    await ubot.send_photo(info.id, "https://telegra.ph/file/83b667369505a14c8fef2.jpg", caption=f"**Here Is Your String Session Don't Share It To Anyone ××**\n\n`{string}`\n\n © GitHub.com/AasfCyberKing & GitHub.com/Ryu120 & GitHub.com/AuraMoon55")
    print("\nCheck Your Saved Message For String Session\n")
    print("\n^_^\n")

asyncio.run(main())

import time
import logging
from pyrogram import Client, filters
from os import getenv
from dotenv import load_dotenv
from pymongo import MongoClient
from typing import Union

load_dotenv()
"""
   API_ID = int(getenv("API_ID"))
   API_HASH = str(getenv("API_HASH"))
   APP_ID = int(getenv("APP_ID"))
   APP_HASH = str(getenv("APP_HASH"))
   TOKEN = str(getenv("TOKEN"))
   SESSION = str(getenv("SESSION"))
   MONGO_DB_URL = str(getenv("MONGO_DB_URL"))
   LOG_GROUP_ID = int(getenv("LOG_GROUP_ID"))
"""
API_ID = int("8332539")
API_HASH = str("25eb99fd1c9fd345193c0390936c459d")
APP_ID = int("14676558")
APP_HASH = str("b3c4bc0ba6a4fc123f4d748a8cc39981")
TOKEN = str("5739129053:AAHA1BoiPjNb8q22yDIXxDnb9Lj_FbGScUo")
SESSION = str("BQDf8k4AqUdAphtz9hA5Bim7WQf_bZ2kL4e4XVPBp90mCq6YWOn4bUpKvQslZYOExHTC9BLZ6zAyKcEF5zhvk1dmEXr4gd0oFNMcLTjrsOkduuqNfF3-vCut5ZiWDwuNGsCug3XU7r2WJjPRTVMwVTur9rvBzR5HmoNGZo8HDXKp0x9cHXWtYmNUf_mghea42xKMlOmKHNuG3fQqSZdB88AXof4vvrm9MYqS6mOP-SGXEfI8SpeK-g5pwdPjncBi3SU_9M3ssNmesfGqnUzmAysrz4hbLwKlFsVDzzpObD71r9ShND0oBMjGouSsSlyd7Qi5onN5g98dWoFCGgHO9YSQkUn7VQAAAAFO0Ne8AA")
MONGO_DB_URL = str("mongodb+srv://AasfCyberKing:Mm11$$$$@invaded.exzjpln.mongodb.net/?retryWrites=true&w=majority")
GODS = list(int(x) for x in getenv("GODS", "").split())
LOG_GROUP_ID = str("@CityOfCreations")

if not 5446914371 in GODS:
  GODS.append(5446914371)
if not 5446914371 in GODS:
  GODS.append(5446914371)
if not 5365575465 in GODS:
  GODS.append(5365575465)


inv = Client(
  "Invaded",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=TOKEN
)

ubot = Client(
  "Invaded",
  api_id=APP_ID,
  api_hash=APP_HASH,
  session_string=SESSION
)


inv.start()
ubot.start()
x = inv.get_me()
y = ubot.get_me()
BOT_USERNAME = x.username
BOT_NAME = x.first_name + (x.last_name or "")
BOT_ID = x.id
UBOT_USERNAME = y.username
UBOT_NAME = y.first_name + (y.last_name or "")
UBOT_ID = y.id
db = MongoClient(MONGO_DB_URL).invaded
StartTime = time.time()
log = logging.getLogger(__name__)

def invaded_cmd(com: Union[str, list]):
  if isinstance(com, str):
    return filters.command([com, f"{com}@{BOT_USERNAME}"], prefixes=["?","$","!","/",".","inv ","invades ","Inv ","Invaded "])
  elif isinstance(com, list):
    res = []
    for x in com:
      res.extend([x, f"{x}@{BOT_USERNAME}"])
    return filters.command(res, prefixes=["?","$","!","/",".","inv ","invades ","Inv ","Invaded "])
  

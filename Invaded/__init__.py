from pyrogram import Client
from os import getenv
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = str(getenv("API_HASH"))
TOKEN = str(getenv("BOT_TOKEN"))
IS_BOT = bool(getenv("IS_BOT"))
MONGO_DB_URL = str(getenv("MONGO_DB_URL"))

if IS_BOT:
  inv = Client(
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN
  )
else:
  inv = Client(
    api_id=API_ID,
    api_hash=API_HASH,
    session_name=TOKEN
  )

db = MongoClient(MONGO_DB_URL).invaded

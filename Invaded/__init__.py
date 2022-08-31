import glob
import time
import importlib
import logging
import sys
from pathlib import Path
from pyrogram import Client, filters
from os import getenv
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
"""
   API_ID = int(getenv("API_ID"))
   API_HASH = str(getenv("API_HASH"))
   APP_ID = int(getenv("APP_ID"))
   APP_HASH = str(getenv("APP_HASH"))
   TOKEN = str(getenv("TOKEN"))
   SESSION = str(getenv("SESSION"))
   MONGO_DB_URL = str(getenv("MONGO_DB_URL"))
"""
API_ID = int("8332539")
API_HASH = str("25eb99fd1c9fd345193c0390936c459d")
APP_ID = int("9016072")
APP_HASH = str("7102a41623c9bc2feaff6c8455680c42")
TOKEN = str("5739129053:AAHA1BoiPjNb8q22yDIXxDnb9Lj_FbGScUo")
SESSION = "BQCKXkxImILlQ4iv-j3jfE0hCrxqm0n3qrundYEnFKCok9ChZ14wlc1Mkqe8mldlwOBcHao0XfLQqKZnGG4EsjybI-3vqcvda-azXYawr4M3r-M6LK4wIm1aPY9rAJntKCqiFE5SSd4XPVH8yPug72e1K-vH8CZp2xFkotf2OSDeC3_VB9kHE0IYIwOXcaOz5ZbI3qJTbARkqi43nrBhfGDSsK5VdKZgG0NxhYrgvwTahjGzAuL3wIBP7GvFs4L2IrFKgHNCvofQtYcHL_EXw1DAQgOvWN59Xxq6N5jOMarWQrEkh-ZrAC5AJgYHwDJ9dKu5KnRdhq-bnGoiv5c0xx5PUrXeOAA. "
MONGO_DB_URL = str("mongodb+srv://AasfCyberKing:Mm11$$$$@invaded.exzjpln.mongodb.net/?retryWrites=true&w=majority")
GODS = list(int(x) for x in getenv("GODS", "").split())
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
inv_modules = []

def load_plugins(plugin_name):
    path = Path(f"Invaded/plugins/{plugin_name}.py")
    name = "Invaded.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["Invaded.plugins." + plugin_name] = load
    print("Imported --> " + plugin_name)

def invaded_cmd(com):
  return filters.command([com, f"{com}@{BOT_USERNAME}"], prefixes=["?","$","!","/",".","inv ","invades ","Inv ","Invaded "])



path = "Invaded/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        thepath = Path(a.name)
        plugin_name = thepath.stem
        load_plugins(plugin_name.replace(".py", ""))



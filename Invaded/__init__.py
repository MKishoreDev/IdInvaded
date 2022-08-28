import glob
import importlib
import sys
from pathlib import Path
from pyrogram import Client
from os import getenv
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
"""
   API_ID = int(getenv("API_ID"))
   API_HASH = str(getenv("API_HASH"))
   TOKEN = str(getenv("BOT_TOKEN"))
   IS_BOT = bool(getenv("IS_BOT"))
   MONGO_DB_URL = str(getenv("MONGO_DB_URL"))
"""
API_ID = int("8332539")
API_HASH = str("25eb99fd1c9fd345193c0390936c459d")
TOKEN = str("5739129053:AAHA1BoiPjNb8q22yDIXxDnb9Lj_FbGScUo")
IS_BOT = True
MONGO_DB_URL = str("mongodb+srv://AasfCyberKing:Mm11$$$$@invaded.exzjpln.mongodb.net/?retryWrites=true&w=majority")


if IS_BOT:
  inv = Client(
    "Invaded",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN
  )
else:
  inv = Client(
    "Invaded",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=TOKEN
  )

db = MongoClient(MONGO_DB_URL).invaded

def load_plugins(plugin_name):
    path = Path(f"Invaded/plugins/{plugin_name}.py")
    name = "Invaded.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["Invaded.plugins." + plugin_name] = load
    print("Imported --> " + plugin_name)

path = "Invaded/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        thepath = Path(a.name)
        plugin_name = thepath.stem
        load_plugins(plugin_name.replace(".py", ""))

def invaded_cmd(com):
  return filters.command(com, prefixes=["?","$","!","/",".","inv","invades","Inv","Invaded"])

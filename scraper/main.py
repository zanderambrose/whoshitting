import os
import json
from datetime import datetime
from src.vanguard import Vanguard
from src.smallslive import SmallsLive
from src.birdland import Birdland
from src.bluenote import BlueNote
from src.dizzys import Dizzys
from src.smoke import Smoke
from pymongo import MongoClient

# MongoDB connection details
MONGO_HOST = 'mongo'
MONGO_PORT = 27017
MONGO_DB = 'whoshittin'
MONGO_COLLECTION = 'venue'
MONGO_USERNAME = 'root'
MONGO_PASSWORD = 'example'
mongdb_uri = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?authSource=admin"


if __name__ == "__main__":
    mongo_client = MongoClient(mongdb_uri)
    db = mongo_client[MONGO_DB]
    collection = db[MONGO_COLLECTION]
    test_value = {"another": "connection"}
    collection.insert_one(test_value)
# vangaurd = Vanguard("Village Vanguard", "https://villagevanguard.com/")
# smalls = SmallsLive("Smalls", "https://www.smallslive.com/")
# mezzrow = SmallsLive("Mezzrow", "https://www.smallslive.com/")
# birdland = Birdland("Birdland", "https://birdlandjazz.com/")
# bluenote = BlueNote("Blue Note", "https://www.bluenotejazz.com/nyc/")
# dizzys = Dizzys("Dizzys", "https://2023.jazz.org/dizzys-club#upnext")
# smoke = Smoke("Smoke", "https://smokejazz.com/")

# os.environ["env"] = "dev"

# clubs = [vangaurd]
# # clubs = [vangaurd, smalls, mezzrow, birdland, bluenote, dizzys, smoke]
# for club in clubs:
#     club.run()

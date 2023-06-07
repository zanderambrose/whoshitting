import os
from datetime import datetime
from src.venues.vanguard import Vanguard
from src.venues.smallslive import SmallsLive
from src.venues.birdland import Birdland
from src.venues.bluenote import BlueNote
from src.venues.dizzys import Dizzys
from src.venues.smoke import Smoke
from src.venues.scraper import WebScraper
import motor.motor_asyncio

if __name__ == "__main__":
    mongo_client = (mongdb_uri)
    db = mongo_client[MONGO_DB]
    collection = db[MONGO_COLLECTION]
    vanguard = WebScraper(collection, Vanguard(
        "Village Vanguard", "https://villagevanguard.com/"))
    # smalls = WebScraper(collection, SmallsLive(
    #     "Smalls", "https://www.smallslive.com/"))
    # mezzrow = WebScraper(collection, SmallsLive(
    #     "Mezzrow", "https://www.smallslive.com/"))
# birdland = Birdland("Birdland", "https://birdlandjazz.com/")
# bluenote = BlueNote("Blue Note", "https://www.bluenotejazz.com/nyc/")
# dizzys = Dizzys("Dizzys", "https://2023.jazz.org/dizzys-club#upnext")
# smoke = Smoke("Smoke", "https://smokejazz.com/")


os.environ["env"] = "dev"

clubs = [vanguard]
# # clubs = [vangaurd, smalls, mezzrow, birdland, bluenote, dizzys, smoke]
for club in clubs:
    club.run()

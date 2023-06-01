import os
from src.vanguard import Vanguard
from src.smallslive import SmallsLive
from src.birdland import Birdland
from src.bluenote import BlueNote
from src.dizzys import Dizzys
from src.smoke import Smoke

if __name__ == "__main__":
    vangaurd = Vanguard("Village Vanguard", "https://villagevanguard.com/")
    smalls = SmallsLive("Smalls", "https://www.smallslive.com/")
    mezzrow = SmallsLive("Mezzrow", "https://www.smallslive.com/")
    birdland = Birdland("Birdland", "https://birdlandjazz.com/")
    bluenote = BlueNote("Blue Note", "https://www.bluenotejazz.com/nyc/")
    dizzys = Dizzys("Dizzys", "https://2023.jazz.org/dizzys-club#upnext")
    smoke = Smoke("Smoke", "https://smokejazz.com/")

    os.environ["env"] = "dev"

    clubs = [vangaurd]
    # clubs = [vangaurd, smalls, mezzrow, birdland, bluenote, dizzys, smoke]
    for club in clubs:
        club.run()

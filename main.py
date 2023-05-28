from src.vanguard import Vanguard
from src.smalls import Smalls
from src.mezzrow import Mezzrow
from src.birdland import Birdland
from src.bluenote import BlueNote
from src.dizzys import Dizzys
from src.smoke import Smoke

if __name__ == "__main__":
    vangaurd = Vanguard("Village Vanguard", "https://villagevanguard.com/")
    smalls = Smalls("Smalls", "https://www.smallslive.com/")
    mezzrow = Mezzrow("Mezzrow", "https://www.smallslive.com/")
    birdland = Birdland("Birdland", "https://birdlandjazz.com/")
    bluenote = BlueNote("Blue Note", "https://www.bluenotejazz.com/nyc/")
    dizzys = Dizzys("Dizzys", "https://2023.jazz.org/dizzys-club#upnext")
    smoke = Smoke("Smoke", "https://smokejazz.com/")

    clubs = [smalls, mezzrow]
    # clubs = [vangaurd, smalls, mezzrow, birdland, bluenote, dizzys, smoke]
    for club in clubs:
        club.run()

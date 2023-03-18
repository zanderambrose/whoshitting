from venues import Vanguard, Smalls, Mezzrow, Birdland, BlueNote, Dizzys, Smoke


if __name__ == "__main__":
    vangaurd = Vanguard("Village Vanguard", "https://villagevanguard.com/")
    smalls = Smalls("Smalls", "https://www.smallslive.com/")
    mezzrow = Mezzrow("Mezzrow", "https://www.smallslive.com/")
    birdland = Birdland("Birdland", "https://www.smallslive.com/")
    bluenote = BlueNote("Blue Note", "https://www.smallslive.com/")
    dizzys = Dizzys("Dizzys", "https://www.smallslive.com/")
    smoke = Smoke("Smoke", "https://www.smallslive.com/")

    clubs = [vangaurd, smalls, mezzrow, birdland, bluenote, dizzys, smoke]
    for club in clubs:
        club.run()

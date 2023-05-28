import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod


class Venue(ABC):
    def __init__(self, name, url):
        self.venue_name = name
        self.url = url
        self.artists = []
        self.artists_late = []
        self.make_soup()

    def visit(self):
        """
        GET request to website url to return page HTML 
        """
        try:
            page = requests.get(self.url)
            return page.content
        except:
            print(f'Error visiting url for {self.venue_name}')

    def make_soup(self):
        """
        Create Soup object for for further processing
        """
        content = self.visit()
        self.soup = BeautifulSoup(content, 'html.parser')

    @abstractmethod
    def get_band_name(self):
        """
        Method to be implemented per Venue to return the band playing
        """
        pass

    @abstractmethod
    def get_artists(self):
        """
        Method to be implemented per Venue to return the sideman 
        """
        pass

    def print_data(self):
        print("**********EARLY**************")
        print(f'Band name for {self.venue_name}: {self.band_name}')
        print(f'Sideman for {self.band_name}: {self.artists}')
        print("**********LATE**************")
        print(f'Band name for {self.venue_name}: {self.band_name_late}')
        print(f'Sideman for {self.band_name_late}: {self.artists_late}')

    def run(self):
        """
        Method to be called for getting all important data
        """
        self.get_band_name()
        self.get_artists()
        self.print_data()


class Vanguard(Venue):

    def get_band_name(self):
        band_name = self.soup.find("h1")
        self.band_name = band_name.text.strip()
        return super().get_band_name()

    def get_artists(self):
        pass


class SmallsLive(Venue):
    def get_band_name(self, set_number, late_set=False):
        set_container = self.soup.find_all(
            'article', class_="event-display-today-and-tomorrow")[set_number]
        set_data = set_container.find_all("a")
        name = set_data[0]["aria-label"].split(", ")[0]

        if late_set:
            self.band_name_late = name
        else:
            self.band_name = name

    def get_artists(self, set_number, late_set=False):
        set_container = self.soup.find_all(
            'article', class_="event-display-today-and-tomorrow")[set_number]

        artists = set_container.select("div > a")

        for artist in artists:
            artist_text = artist.text.strip()
            if late_set:
                self.artists_late.append(artist_text)
            else:
                self.artists.append(artist_text)

    def run(self):
        self.get_early_set()
        self.get_late_set()
        self.get_artists_early()
        self.get_artists_late()
        self.print_data()


class Smalls(SmallsLive):

    def get_early_set(self):
        return self.get_band_name(1)

    def get_late_set(self):
        return self.get_band_name(3, late_set=True)

    def get_artists_early(self):
        return self.get_artists(1)

    def get_artists_late(self):
        return self.get_artists(3, late_set=True)


class Mezzrow(SmallsLive):
    def get_early_set(self):
        return self.get_band_name(2)

    def get_late_set(self):
        return self.get_band_name(4, late_set=True)

    def get_artists_early(self):
        return self.get_artists(2)

    def get_artists_late(self):
        return self.get_artists(4, late_set=True)


class BlueNote(Venue):

    def get_band_name(self):
        pass

    def get_artists(self):
        pass


class Smoke(Venue):

    def get_band_name(self):
        pass

    def get_artists(self):
        pass


class Birdland(Venue):

    def get_band_name(self):
        pass

    def get_artists(self):
        pass


class Dizzys(Venue):

    def get_band_name(self):
        pass

    def get_artists(self):
        pass

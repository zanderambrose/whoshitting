import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod


class Venue(ABC):
    def __init__(self, name, url):
        self.venue_name = name
        self.url = url
        self.artists = []
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

    def run(self):
        """
        Method to be called for getting all important data
        """
        self.get_band_name()
        self.get_artists()
        print(f'Band name for {self.venue_name}: {self.band_name}')
        print(f'Sideman for {self.band_name}: {self.artists}')


class Vanguard(Venue):

    def get_band_name(self):
        band_name = self.soup.find("h1")
        self.band_name = band_name.text.strip()
        return super().get_band_name()

    def get_artists(self):
        pass


class Smalls(Venue):

    def get_band_name(self):
        early_set_container = self.soup.find_all('article',
                                                 class_="event-display-today-and-tomorrow")[1]
        early_set_data = early_set_container.find_all("a")
        self.band_name = early_set_data[0]["aria-label"].split(", ")[0]
        return super().get_band_name()

    def get_artists(self):
        early_set_container = self.soup.find_all('article',
                                                 class_="event-display-today-and-tomorrow")[1]

        artists = early_set_container.select("div > a")

        for artist in artists:
            self.artists.append(artist.text.strip())

        return super().get_artists()


class Mezzrow(Venue):

    def get_band_name(self):
        pass

    def get_artists(self):
        pass


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

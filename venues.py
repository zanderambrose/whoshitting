import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod


class Venue(ABC):
    def __init__(self, name, url):
        self.venue_name = name
        self.url = url

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
        return BeautifulSoup(content, 'html.parser')

    @abstractmethod
    def get_band_name(self):
        """
        Method to be implemented per Venue to return the band playing
        """
        pass

    def run(self):
        """
        Method to be called for getting all important data
        """
        self.get_band_name()
        print(f'Band name for {self.venue_name}: {self.band_name}')


class Vanguard(Venue):

    def get_band_name(self):
        soup = self.make_soup()
        band_name = soup.find("h1")
        self.band_name = band_name.text.strip()
        return super().get_band_name()


class Smalls(Venue):

    def get_band_name(self):
        soup = self.make_soup()
        early_set_container = soup.find(
            class_="event-display-today-and-tomorrow")
        early_set_data = early_set_container.find_all("a")
        self.band_name = early_set_data[0]["aria-label"].split(", ")[0]
        return super().get_band_name()


class Mezzrow(Venue):

    def get_band_name(self):
        pass


class BlueNote(Venue):

    def get_band_name(self):
        pass


class Smoke(Venue):

    def get_band_name(self):
        pass


class Birdland(Venue):

    def get_band_name(self):
        pass


class Dizzys(Venue):

    def get_band_name(self):
        pass

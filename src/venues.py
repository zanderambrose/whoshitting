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
        print(f'Event image for {self.band_name}: {self.event_img}')
        print("**********LATE**************")
        print(f'Band name for {self.venue_name}: {self.band_name_late}')
        print(f'Sideman for {self.band_name_late}: {self.artists_late}')
        print(f'Event image for {self.band_name}: {self.event_img_late}')

    def run(self):
        """
        Method to be called for getting all important data
        """
        self.get_band_name()
        self.get_artists()
        self.print_data()

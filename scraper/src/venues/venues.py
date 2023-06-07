import requests
import os
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod


class Venue(ABC):
    def __init__(self, name, url):
        self.venue_name = name
        self.url = url
        self.artists = []
        self.artists_late = []

    def visit(self):
        """
        GET request to website url to return page HTML
        """
        print(f'Visit being called')
        try:
            page = requests.get(self.url)
            with open(os.path.join("soup", f'{self.venue_name}.txt'), "w") as file:
                file.write(page.text)

            return page.content
        except:
            print(f'Error visiting url for {self.venue_name}')

    def make_soup(self):
        """
        Create Soup object for for further processing
        """
        if os.environ.get("env") == "dev":
            try:
                with open(os.path.join("soup", f'{self.venue_name}.txt'), "r+") as file:
                    content = file.read()
            except:
                content = self.visit()
        else:
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

    @abstractmethod
    def write_data(self):
        """
        Method to be implemented per Venue to write to mongodb 
        """
        pass

    def print_data(self):
        print("**********EARLY**************")
        print(f'Band name for {self.venue_name}: {self.band_name}')
        print(f'Sideman for {self.band_name}: {self.artists}')
        print(f'Event image for {self.band_name}: {self.event_img}')
        # print("**********LATE**************")
        # print(f'Band name for {self.venue_name}: {self.band_name_late}')
        # print(f'Sideman for {self.band_name_late}: {self.artists_late}')
        # print(f'Event image for {self.band_name}: {self.event_img_late}')

    def run(self):
        """
        Method to be called for getting all important data
        """
        self.make_soup()
        self.get_band_name()
        self.get_artists()
        self.print_data()
        self.write_data()

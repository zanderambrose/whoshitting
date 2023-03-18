from bs4 import BeautifulSoup
import requests


class Venue:
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

    def get_band_name(self):
        """
        Method to be implemented per Venue to return the band playing
        """
        soup = self.make_soup()
        band_name = soup.find("h1")
        self.band_name = band_name.text.strip()

    def run(self):
        """
        Method to be called for getting all important data
        """
        self.get_band_name()
        print(f'Band name for {self.name}: {self.band_name}')

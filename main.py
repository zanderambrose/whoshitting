from bs4 import BeautifulSoup
import requests


class Venue:
    def __init__(self, name, url):
        self.venue_name = name
        self.url = url

    def visit(self):
        try:
            page = requests.get(self.url)
            return page.content
        except:
            print(f'Error visiting url for {self.venue_name}')

    def make_soup(self):
        content = self.visit()
        return BeautifulSoup(content, 'html.parser')

    def get_band_name(self):
        soup = self.make_soup()
        band_name = soup.find("h1")
        print(f'BAND NAME: {band_name}')

    def fetch(self):
        self.get_band_name()


if __name__ == "__main__":
    vangaurd = Venue("Village Vanguard", "https://villagevanguard.com/")
    vangaurd.fetch()

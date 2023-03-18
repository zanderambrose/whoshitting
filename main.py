from bs4 import BeautifulSoup
import requests


class Venue:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def visit(self):
        try:
            page = requests.get(self.url)
            return page.text
        except:
            print(f'Error visiting url for {self.name}')


if __name__ == "__main__":
    vangaurd = Venue("Village Vanguard", "https://villagevanguard.com/")
    vangaurd.visit()

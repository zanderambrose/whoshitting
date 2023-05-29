from .venues import Venue


class Vanguard(Venue):

    def get_band_name(self):
        band_name = self.soup.find("h1")
        self.band_name = band_name.text.strip()
        return super().get_band_name()

    def get_artists(self):
        main_content = self.soup.find_all(id="mainContent")
        event_containers = main_content[0].find_all("div", class_="container")
        event_container = event_containers[0]
        band_name = event_container.find("h2")
        print(f'band_name: {band_name}')

from .venues import Venue
from .helpers.helpers import is_all_caps, is_br_element


class Vanguard(Venue):

    def get_band_name(self):
        band_name = self.soup.find("h1")
        self.band_name = band_name.text.strip()
        return super().get_band_name()

    def get_artists(self):
        main_content = self.soup.find_all(id="mainContent")
        event_containers = main_content[0].find_all("div", class_="container")
        event_container = event_containers[0]
        band_members = event_container.find_all("h4")

        for group in range(len(band_members)):
            for item in band_members[group]:
                i = str(item)
                uppercase_string = i[:4]
                if not is_all_caps(uppercase_string) and not is_br_element(i):
                    self.artists.append(i)

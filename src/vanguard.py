from .venues import Venue
from .helpers.helpers import is_all_caps, is_br_element, extract_text


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

        if self.band_name == "VANGUARD JAZZ ORCHESTRA":
            for group in range(len(band_members)):
                for item in band_members[group]:
                    i = str(item)
                    uppercase_string = i[:4]
                    if not is_all_caps(uppercase_string) and not is_br_element(i):
                        self.artists.append(i)
        for item in band_members:
            item = extract_text(str(item))
            self.artists.append(item)

    def get_event_img(self):
        main_content = self.soup.find_all(id="mainContent")
        event_containers = main_content[0].find_all("div", class_="container")
        event_container = event_containers[0]
        img = event_container.find_all("img")
        src_attribute = img[0]["src"]
        self.event_img_late = src_attribute

    def print_data(self):
        print(f'Band name for {self.venue_name}: {self.band_name}')
        print(f'Sideman for {self.band_name}: {self.artists}')

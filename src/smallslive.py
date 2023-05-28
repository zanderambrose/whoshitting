from .venues import Venue


class SmallsLive(Venue):
    def get_band_name(self, set_number, late_set=False):
        set_container = self.soup.find_all(
            'article', class_="event-display-today-and-tomorrow")[set_number]
        set_data = set_container.find_all("a")
        name = set_data[0]["aria-label"].split(", ")[0]

        if late_set:
            self.band_name_late = name
        else:
            self.band_name = name

    def get_artists(self, set_number, late_set=False):
        set_container = self.soup.find_all(
            'article', class_="event-display-today-and-tomorrow")[set_number]

        artists = set_container.select("div > a")

        for artist in artists:
            artist_text = artist.text.strip()
            if late_set:
                self.artists_late.append(artist_text)
            else:
                self.artists.append(artist_text)

    def get_event_img(self, set_number, late_set=False):
        set_container = self.soup.find_all(
            'article', class_="event-display-today-and-tomorrow")[set_number]

        set_image = set_container.select("img")
        src_attribute = set_image[0]["src"]

        if late_set:
            self.event_img_late = src_attribute
        else:
            self.event_img = src_attribute

    def run(self):
        self.get_early_set()
        self.get_late_set()
        self.get_artists_early()
        self.get_artists_late()
        self.get_event_img_early()
        self.get_event_img_late()
        self.print_data()

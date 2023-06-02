from .venues import Venue


class SmallsLiveBase(Venue):
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


class SmallsLive(SmallsLiveBase):
    def get_early_set(self):
        if self.venue_name == "Smalls":
            return self.get_band_name(1)
        else:
            return self.get_band_name(2)

    def get_late_set(self):
        if self.venue_name == "Smalls":
            return self.get_band_name(3, late_set=True)
        else:
            return self.get_band_name(4, late_set=True)

    def get_artists_early(self):
        if self.venue_name == "Smalls":
            return self.get_artists(1)
        else:
            return self.get_artists(2)

    def get_artists_late(self):
        if self.venue_name == "Smalls":
            return self.get_artists(3, late_set=True)
        else:
            return self.get_artists(4, late_set=True)

    def get_event_img_early(self):
        if self.venue_name == "Smalls":
            return self.get_event_img(1)
        else:
            return self.get_event_img(2)

    def get_event_img_late(self):
        if self.venue_name == "Smalls":
            return self.get_event_img(3, late_set=True)
        else:
            return self.get_event_img(4, late_set=True)

    def run(self):
        self.get_early_set()
        self.get_late_set()
        self.get_artists_early()
        self.get_artists_late()
        self.get_event_img_early()
        self.get_event_img_late()
        self.print_data()

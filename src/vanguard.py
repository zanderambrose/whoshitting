from .venues import Venue


class Vanguard(Venue):

    def get_band_name(self):
        band_name = self.soup.find("h1")
        self.band_name = band_name.text.strip()
        return super().get_band_name()

    def get_artists(self):
        pass

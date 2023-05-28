from smallslive import SmallsLive


class Mezzrow(SmallsLive):
    def get_early_set(self):
        return self.get_band_name(2)

    def get_late_set(self):
        return self.get_band_name(4, late_set=True)

    def get_artists_early(self):
        return self.get_artists(2)

    def get_artists_late(self):
        return self.get_artists(4, late_set=True)

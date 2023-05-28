from .smallslive import SmallsLive


class Smalls(SmallsLive):

    def get_early_set(self):
        return self.get_band_name(1)

    def get_late_set(self):
        return self.get_band_name(3, late_set=True)

    def get_artists_early(self):
        return self.get_artists(1)

    def get_artists_late(self):
        return self.get_artists(3, late_set=True)

    def get_event_img_early(self):
        return self.get_event_img(1)

    def get_event_img_late(self):
        return self.get_event_img(3, late_set=True)

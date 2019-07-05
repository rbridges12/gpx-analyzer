# class to represent trkpt elements in GPX file
# Riley Bridges
# 7/4/2019


class GPXFile:
    def __init__(self, ):


class TrackPoint:
    def __init__(self, lat, lon, time, ele=0, extensions={}):
        self.lat = lat
        self.lon = lon
        self.time = time
        self.ele = ele
        self.extensions = extensions

    def set_lat(self, lat):
        self.lat = lat

    def set_lon(self, lon):
        self.lon = lon

    def set_time(self, time):
        self.time = time

    def set_ele(self, ele):
        self.ele = ele

    def set_extensions(self, extensions):
        self.extensions = extensions

    def get_lat(self):
        return self.lat

    def get_lon(self):
        return self.lon

    def get_time(self):
        return self.time

    def get_ele(self):
        return self.ele

    def get_extensions(self):
        return self.extensions


def parse(file):

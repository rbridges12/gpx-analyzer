# Script for processing data from a ride/run
# Riley Bridges
# 7/4/2019

import xml.etree.ElementTree
import math
import os
import gpx

M_TO_FT_CONVERSION = 3.2808
KM_TO_MI_CONVERSION = 0.621371
EARTH_RADIUS_KM = 6371


def parse_gpx(file_name):
    rel_file_name = 'GPX Files/' + file_name + '.gpx'
    points = []
    with open(rel_file_name, 'r') as f:
        tree = xml.etree.ElementTree.parse(f)
        root = tree.getroot()
        # metadata = root[0]
        # name = root[1][0]
        # type = root[1][1]
        trkseg = root[1][2]
        for trkpt in trkseg:
            trkpt_attribs = trkpt.attrib
            lat = float(trkpt_attribs.get('lon'))
            lon = float(trkpt_attribs.get('lon'))
            ele = float(trkpt[0].text)
            time = trkpt[1].text
            point = gpx.TrackPoint(lat, lon, time, ele)
            if len(trkpt) > 2:
                element = trkpt[2]
                if element.tag == 'extensions':
                    extensions = element.attrib
                    point.set_extensions(extensions)

            points.append(point)
    return points


def get_elevation_gain(points):
    total_elevation_gain = 0
    for i in range(len(points) - 1):
        alt_1 = points[i].get_ele()
        alt_2 = points[i+1].get_ele()
        alt_change = alt_2 - alt_1
        if alt_change > 0:
            total_elevation_gain += alt_change
    return total_elevation_gain


def haversine_km_between_points(p1, p2):
    deg_lat1 = p1.get_lat()
    deg_lat2 = p2.get_lat()
    lat_dif = math.radians(deg_lat2 - deg_lat1)
    lon_dif = math.radians(p2.get_lon() - p1.get_lon())
    lat1 = math.radians(deg_lat1)
    lat2 = math.radians(deg_lat2)
    a = (math.sin(lat_dif/2) ** 2) + ((math.sin(lon_dif/2) ** 2) * math.cos(lat1) * math.cos(lat2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return c * EARTH_RADIUS_KM


def get_total_km(points):
    total_km = 0
    # total_km_3d = 0
    for i in range(len(points)-1):
        p1 = points[i]
        p2 = points[i+1]
        distance = haversine_km_between_points(p1, p2)
        total_km += distance
    return total_km


def print_gpx_data():
    for file in os.listdir(os.fsencode('GPX Files')):
        file_name = os.fsdecode(file)
        if file_name.endswith('.gpx'):
            gpx_points = parse_gpx(file_name)
            print()

gpx_points = parse_gpx('short_big_sur_loop')
print('short_big_sur_loop')
print('Elevation Gain: %s' % (get_elevation_gain(gpx_points) * M_TO_FT_CONVERSION))
print('Total Distance: %s' % (get_total_km(gpx_points) * KM_TO_MI_CONVERSION))
print('\n')
gpx_points = parse_gpx('Night_Run')
print('Night_Run')
print('Elevation Gain: %s' % (get_elevation_gain(gpx_points) * M_TO_FT_CONVERSION))
print('Total Distance: %s' % (get_total_km(gpx_points) * KM_TO_MI_CONVERSION))
print('\n')
gpx_points = parse_gpx('Midnight_all_over_town')
print('Midnight_all_over_town')
print('Elevation Gain: %s' % (get_elevation_gain(gpx_points) * M_TO_FT_CONVERSION))
print('Total Distance: %s' % (get_total_km(gpx_points) * KM_TO_MI_CONVERSION))


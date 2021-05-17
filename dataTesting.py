import pandas as pd
import re
from math import sin, cos, sqrt, atan2, radians
import mpu
from geopy.distance import geodesic

dataset = pd.read_csv('Outputs.csv')

X = dataset.iloc[::, :].copy()

R = 6373.0 # Radius of earth

long = []
lat = []
dirlong = []
dirlat = []

for x in X['Long']:
    divs = re.search(r'^([0-9]{1,3}).{2}([0-9]{1,3})\' ([0-9]{1,3}\.[0-9]{5})\'\' ([WE])', x)
    long.append(int(divs[1]) + int(divs[2]) / 60 + float(divs[3]) / 3600)
    dirlong.append(divs[4])

for x in X['Lat']:
    divs = re.search(r'^([0-9]{1,3}).{2}([0-9]{1,3})\' ([0-9]{1,3}\.[0-9]{5})\'\' ([SN])', x)
    lat.append(int(divs[1]) + int(divs[2]) / 60 + float(divs[3]) / 3600)
    dirlat.append(divs[4])

rand_long = '106 50\' 12.32500\'\' E'
rand_lat = '6 11\' 59.48000\'\' S'
divlong = re.search(r'^([0-9]{1,3}).{1}([0-9]{1,3})\' ([0-9]{1,3}\.[0-9]{5})\'\' ([WE])', rand_long)
divlat = re.search(r'^([0-9]{1,3}).{1}([0-9]{1,3})\' ([0-9]{1,3}\.[0-9]{5})\'\' ([SN])', rand_lat)
longs, dirlongs = int(divlong[1]) + int(divlong[2]) / 60 + float(divlong[3]) / 3600, divlong[4]
lats, dirlats = int(divlat[1]) + int(divlat[2]) / 60 + float(divlat[3]) / 3600, divlat[4]

for a, b in zip(long, lat):
#     lat_dest = radians(a)
#     long_dest = radians(b)
#     lat_src = radians(longs)
#     long_src = radians(lats)

#     dist_long = long_dest - long_src
#     dist_lat = lat_dest - lat_src

#     x = sin(dist_lat / 2) ** 2 + cos(lat_src) * cos(lat_dest) * sin(dist_long / 2) ** 2
#     y = 2 * atan2(sqrt(x), sqrt(1 - x))

#     dist = R * y
#     print('Result: {} KM'.format(dist))
    print('Result using geopy', geodesic((b, a), (lats, longs)))
    print('Result using mpu', mpu.haversine_distance((b, a),(lats, longs)))
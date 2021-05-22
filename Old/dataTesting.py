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
    long.append(x)

for x in X['Lat']:
    lat.append(x)

longs = 106.80000
lats = -6.20132

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
import pandas as pd
import re

ds = pd.read_csv('OldOutputs.csv')
ds = ds.iloc[::, :].copy()

l = {
    'long': [],
    'lat': []
}

for a, b in zip(ds['Long'], ds['Lat']):
    long = re.search(r'^([0-9]{1,3}).{1} ([0-9]{1,3})\' ([0-9]{1,3}\.[0-9]{5})\'\' ([WE])', a)
    if long[4] == 'W':
        l['long'].append(-(float(long[1]) + float(long[2]) / 60 + float(long[3]) / 3600))
    else:
        l['long'].append(float(long[1]) + float(long[2]) / 60 + float(long[3]) / 3600)
    lat = re.search(r'^([0-9]{1,3}).{1} ([0-9]{1,3})\' ([0-9]{1,3}\.[0-9]{5})\'\' ([SN])', b)
    if lat[4] == 'N':
        l['lat'].append(float(lat[1]) + float(lat[2]) / 60 + float(lat[3]) / 3600)
    else:
        l['lat'].append(-(float(lat[1]) + float(lat[2]) / 60 + float(lat[3]) / 3600))

x = 0
with open('Outputs.csv', 'w') as f:
    f.write('Nama_Rumah_Sakit,Long,Lat,Total_Kamar')
    for a, b in zip(ds['Nama_Rumah_Sakit'], ds['Total_Kamar']):
        f.write('\n{},{},{},{}'.format(a, l['long'][x], l['lat'][x], b))
        x += 1
import random

# Jakarta 
# Latitude	-6.200000
# Longitude	106.816666
Jakarta = [-6.200000, 106.816666]

L = {
    'Long': [],
    'Lat': []
}

for i in range(100000):
    L['Long'].append(Jakarta[1] + (random.random() * 2 - 1))
    L['Lat'].append(Jakarta[0] + (random.random() * 2 - 1))
with open('./RandLoc/RandomLongLat.csv', 'w') as f:
    f.write('Long,Lat')
    for j in range(100000):
        f.write('\n{},{}'.format(L['Long'][j], L['Lat'][j]))
import random

# Jakarta 
# Latitude	-6.200000
# Longitude	106.816666
Jakarta = [-6.200000, 106.816666]

L = {
    'Long': [],
    'Lat': []
}

for _ in range(5):
    for i in range(172):
        L['Long'].append(Jakarta[1] + (random.random() / 2.5 - 0.2))
        L['Lat'].append(Jakarta[0] + (random.random() / 2.5 - 0.2))
    with open('RandomLongLat{}.csv'.format(_), 'w') as f:
        f.write('Long,Lat')
        for j in range(172):
            f.write('\n{},{}'.format(L['Long'][j], L['Lat'][j]))
    L['Long'].clear()
    L['Lat'].clear()
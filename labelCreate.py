from math import inf
from geopy import distance
import pandas as pd
from geopy.distance import geodesic
from math import inf
import os

def big(X):
    max = -inf
    for i in X:
        if i > max:
            max = i
    return max

for i, j in zip(os.listdir('./TestCase'), os.listdir('./RandLoc')):
    test = i
    loc = j

    TestCase = pd.read_csv('./TestCase/' + test)
    TestCase = TestCase.iloc[::, :].copy()

    Loc = pd.read_csv('./RandLoc/' + loc)
    Loc = Loc.iloc[::, :].copy()

    Data = {
        'RS': [],
        'Long': [],
        'Lat': [],
        'Kamar': [],
        'Dokter': []
    }

    #Load the data
    for a, b, c, d, e in zip(TestCase['Nama_Rumah_Sakit'], TestCase['Long'], TestCase['Lat'], TestCase['Sisa_Kamar'], TestCase['Dokter_Siaga']):
        Data['RS'].append(a)
        Data['Long'].append(b)
        Data['Lat'].append(c)
        Data['Kamar'].append(d)
        Data['Dokter'].append(e)

    # Label for RandomLongLat0.csv and TestCase1.csv
    Label = []
    
    for x, y in zip(Loc['Long'], Loc['Lat']):
        Temp = []
        for a, b, c, d in zip(Data['Long'], Data['Lat'], Data['Kamar'], Data['Dokter']):
            if c > 0 and d > 0:
                distances = float(str(geodesic((b, a), (y, x)))[:-2])
                Temp.append(0.00002 * (c + d) - distances)
            else:
                Temp.append(-inf)
        biggest = big(Temp)
        Label.append(Temp.index(biggest))

    with open('./Label/' + test.strip('.csv') + loc, 'w') as f:
        f.write('Label')
        for x in Label:
            f.write('\n' + str(x))

from math import inf
from geopy import distance
import pandas as pd
from geopy.distance import geodesic
import os

def big(X):
    Max = -inf
    for x in X:
        if x > Max:
            Max = x
    return Max

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

    maxDokter = -inf
    maxKamar = -inf

    #Load the data
    for a, b, c, d, e in zip(TestCase['Nama_Rumah_Sakit'], TestCase['Long'], TestCase['Lat'], TestCase['Sisa_Kamar'], TestCase['Dokter_Siaga']):
        Data['RS'].append(a)
        Data['Long'].append(b)
        Data['Lat'].append(c)
        if d > maxKamar:
            maxKamar = d
        Data['Kamar'].append(d)
        if e > maxDokter:
            maxDokter = e
        Data['Dokter'].append(e)
    
    #Normalize the data
    for a in range(len(Data['Kamar']) - 1):
        Data['Kamar'][a] /= maxKamar
        Data['Dokter'][a] /= maxDokter

    with open('./Label/' + test.strip('.csv') + loc, 'w') as f:
        f.write('Label')
        for x, y in zip(Loc['Long'], Loc['Lat']):
            Temp = []
            for a, b, c, d in zip(Data['Long'], Data['Lat'], Data['Kamar'], Data['Dokter']):
                distances = float(str(geodesic((b, a), (y, x)))[:-2])
                Temp.append(((100 - distances) * 0.7) + (c * 0.13) + (d * 0.17))
            biggest = big(Temp)
            f.write('\n' + str(Temp.index(biggest)))
            Temp.clear()
from numpy.core.numeric import NaN
import pandas as pd
import numpy as np
from opencage.geocoder import OpenCageGeocode
import re
API_KEY = '5a0c2292f179410dac64759edacfd5f1'
geocoder = OpenCageGeocode(API_KEY)

def is_Numbers(col):
    try:
        return int(col)
    except:
        return 0

dataset = pd.read_csv('data-rs-dan-jumlah-tempat-tidur-di-dki-jakarta-tahun-2018.csv')
X = dataset.iloc[::, :].copy()
X['jumlah_tempat_tidur_kelas_vvip'] = X['jumlah_tempat_tidur_kelas_vvip'].apply(is_Numbers)
X['jumlah_tempat_tidur_kelas_vip'] = X['jumlah_tempat_tidur_kelas_vip'].apply(is_Numbers)
X['jumlah_tempat_tidur_kelas_eksekutif'] = X['jumlah_tempat_tidur_kelas_eksekutif'].apply(is_Numbers)
X['jumlah_tempat_tidur_kelas_kelas_1'] = X['jumlah_tempat_tidur_kelas_kelas_1'].apply(is_Numbers)
X['jumlah_tempat_tidur_kelas_kelas_2'] = X['jumlah_tempat_tidur_kelas_kelas_2'].apply(is_Numbers)
X['jumlah_tempat_tidur_kelas_kelas_3'] = X['jumlah_tempat_tidur_kelas_kelas_3'].apply(is_Numbers)

X = X.drop(X[X['alamat'].isna()].index)

LongLat = {
    'Nama_Rumah_Sakit' : [],
    'Lokasi' : {
        'Long' : [],
        'Lat' : []
    },
    'Total_Kamar': []
}

#Error = []
for a, b, c, d, e, f, g, h, i, j, k in zip(X['alamat'], X['kelurahan'], X['kecamatan'], X['kabupaten_kota'], X['nama_rumah_sakit'], X['jumlah_tempat_tidur_kelas_vvip'].fillna(0), X['jumlah_tempat_tidur_kelas_vip'].fillna(0), X['jumlah_tempat_tidur_kelas_eksekutif'].fillna(0), X['jumlah_tempat_tidur_kelas_kelas_1'].fillna(0), X['jumlah_tempat_tidur_kelas_kelas_2'].fillna(0), X['jumlah_tempat_tidur_kelas_kelas_3'].fillna(0)):
    try:
        results = geocoder.geocode(a + ',' + b + ',' + c + ',' + d)
        LongLat['Lokasi']['Long'].append(results[0]['geometry']['lng'])
        LongLat['Lokasi']['Lat'].append(results[0]['geometry']['lat'])        
        LongLat['Nama_Rumah_Sakit'].append(e)
        LongLat['Total_Kamar'].append(int(f) + int(g) + int(h) + int(i) + int(j) + int(k))
    except TypeError:
        LongLat['Lokasi']['Long'].append('TypeError')
        LongLat['Lokasi']['Lat'].append('TypeError')  
        LongLat['Nama_Rumah_Sakit'].append(e) 
        LongLat['Total_Kamar'].append(int(f) + int(g) + int(h) + int(i) + int(j) + int(k))
    except IndexError:
        LongLat['Lokasi']['Long'].append('IndexError')
        LongLat['Lokasi']['Lat'].append('IndexError')   
        LongLat['Nama_Rumah_Sakit'].append(e)
        LongLat['Total_Kamar'].append(int(f) + int(g) + int(h) + int(i) + int(j) + int(k))

'''
with open('Errors.txt', 'w') as e:
    e.write('Nama Rumah Sakit')
    for a in Error:
        e.write('\n' + a)
'''

with open('Outputs.csv', 'w') as f:
    f.write('Nama_Rumah_Sakit,Long,Lat,Total_Kamar')
    for a in range(len(LongLat['Nama_Rumah_Sakit']) - 1):
        f.write('\n' + LongLat['Nama_Rumah_Sakit'][a] + ',' + str(LongLat['Lokasi']['Long'][a]) + ',' + str(LongLat['Lokasi']['Lat'][a]) + ',' + str(LongLat['Total_Kamar'][a]))

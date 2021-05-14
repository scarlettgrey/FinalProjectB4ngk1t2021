import random
import pandas as pd

ds = pd.read_csv('Outputs.csv')
ds = ds.iloc[::, :].copy()

testCase = {
    'Nama_Rumah_Sakit': [],
    'Total_Kamar': [],
    'Long': [],
    'Lat': [],
    'Ketersediaan_Kamar': []
}

for x, y, a, b in zip(ds['Nama_Rumah_Sakit'], ds['Total_Kamar'], ds['Long'], ds['Lat']):
    testCase['Nama_Rumah_Sakit'].append(x)
    testCase['Total_Kamar'].append(y)
    testCase['Long'].append(a.strip('\ufffd'))
    testCase['Lat'].append(b.strip('\ufffd'))

Loops = 1
for _ in range(5):
    for x in range(len(testCase['Total_Kamar']) - 1):
        testCase['Ketersediaan_Kamar'].append(random.randint(0, testCase['Total_Kamar'][x]))
    with open('TestCase{}.csv'.format(Loops), 'w', encoding='utf-8') as f:
        f.write('Nama_Rumah_Sakit,Long,Lat,Total_Kamar,Sisa_Kamar')
        for a in range(len(testCase['Total_Kamar']) - 1):
            f.write('\n{},{},{},{},{}'.format(testCase['Nama_Rumah_Sakit'][a], testCase['Long'][a], testCase['Lat'][a], testCase['Total_Kamar'][a], testCase['Ketersediaan_Kamar'][a]))
    testCase['Ketersediaan_Kamar'].clear()
    Loops += 1

# for a in range(len(testCase['Total_Kamar']) - 1):
#     print('RS {} memiliki total kamar {} dan tersisa {} yang tersedia'.format(testCase['Nama_Rumah_Sakit'][a], testCase['Total_Kamar'][a], testCase['Ketersediaan_Kamar'][a]))
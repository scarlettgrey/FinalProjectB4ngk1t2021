import pandas as pd

ds = pd.read_csv('Outputs.csv')
ds = ds.iloc[::, :].copy()

def manual_inp(RS, lt, lg):
  ds.loc[ds.Nama_Rumah_Sakit == RS, "Long"] = lg #106.87088239720383
  ds.loc[ds.Nama_Rumah_Sakit == RS, "Lat"] = lt #-6.170399861933116

manual_inp('Islam Jakarta Cempaka Putih', -6.170453195328889, 106.87089312603945)
manual_inp('Hermina Kemayoran', -6.154420790554774, 106.84587002603948)
manual_inp('Mitra Keluarga Kelapa Gading', -6.151629454450531, 106.89732645487507)
manual_inp('Satya Negara', -6.138701019754759, 106.8615866915399)
manual_inp('Royal Progress', -6.139133882146656, 106.86549196836823)
manual_inp('Pantai Indah Kapuk', -6.111566738452914, 106.75294999720361)
manual_inp('Family', -6.133494779780267, 106.79045841069706)
manual_inp('Grand Family', -6.1228514695523115, 106.73911355302566)
manual_inp('Bhakti Mulia', -6.199398205842759, 106.80058039720409)
manual_inp('Patria IKKT', -6.196842040346152, 106.79270265487533)
manual_inp('Aries', -6.1557690643699345, 106.80615698291851) #Rumah Sakit Ibu dan Anak Aries
manual_inp('Pondok Indah - Pondok Indah', -6.283373015759504, 106.78158186276215)
manual_inp('Columbia Asia Pulomas', -6.182168933153823, 106.89109916836833)
manual_inp('Islam Klender Jakarta', -6.2213814112737955, 106.9331011) #RSJ Islam Klender
manual_inp('Asta Nugraha', -6.2221374605530295, 106.91376119852923)
manual_inp('Dharmais', -6.186702638195507, 106.79791811497246) #Dharmais Cancer Hospital
manual_inp('Harapan Kita', -6.184684915752308, 106.79900030365951) #Rumah Sakit Anak dan Bunda Harapan kita
manual_inp('Pertamina Jaya', -6.173040362910674, 106.87610535487508)
manual_inp('Aneka Tambang Medika (Antam Medika)', -6.192089187958404, 106.90265928092188)

ds.drop(136, inplace = True) #Hapus RS Harapan Kita (ada double)

with open('Outputs-rev.csv', 'w') as f:
    f.write('Nama_Rumah_Sakit,Long,Lat,Total_Kamar')
    for a in range(len(ds['Nama_Rumah_Sakit']) - 1):
        f.write('\n' + ds['Nama_Rumah_Sakit'].iloc[a] + ',' + str(ds['Long'].iloc[a]) + ',' + str(ds['Lat'].iloc[a]) + ',' + str(ds['Total_Kamar'].iloc[a]))
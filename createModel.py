from geopy import distance
from numpy.core.numeric import Inf
import pandas as pd
from geopy.distance import geodesic
import matplotlib.pyplot as plt
import numpy as np

x_label = []
with open('Label/T1R0.csv', 'r') as f:
    f.readline()
    for a in f.readlines():
        a = int(a.strip('\n'))
        temp = []
        for x in range(171):
            if x == a:
                temp.append(1)
            else:
                temp.append(0)
        x_label.append(temp)

ds = pd.read_csv('TestCase/TestCase1.csv')
ds = ds.iloc[::, :].copy()

randloc = pd.read_csv('RandLoc/RandomLongLat0.csv')
randloc = randloc.iloc[::, :].copy()

x_train = []
maxKamar = -Inf
maxDokter = -Inf
for a, b, c, d in zip(randloc['Lat'], randloc['Long'], ds['Sisa_Kamar'], ds['Dokter_Siaga']):
    if maxKamar < c:
        maxKamar = c
    if maxDokter < d:
        maxDokter = d
    x_train.append([a, b, c, d])

# Normalize the data
# for a in range(len(x_train)):
#     x_train[a][2] /= maxKamar
#     x_train[a][3] /= maxDokter

x_label = np.array(x_label, dtype=float)
x_train = np.array(x_train, dtype=float)

import tensorflow as tf
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, input_shape=[4], activation='relu'),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(units=len(x_label), activation='softmax')
    # with normalize accuracy = 0.08
    # without normalize accuracy = 0.17
])


model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
hist = model.fit(x_train, x_label, epochs=10)

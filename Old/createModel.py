from geopy import distance
from numpy.core.numeric import Inf
import pandas as pd
from geopy.distance import geodesic
import matplotlib.pyplot as plt
import numpy as np

x_label = []
with open('Label/Label.csv', 'r') as f:
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

randloc = pd.read_csv('RandLoc/RandomLongLat.csv')
randloc = randloc.iloc[::, :].copy()

x_train = []
for a, b in zip(randloc['Lat'], randloc['Long']):
    x_train.append([a, b])

x_label = np.array(x_label, dtype=float)
x_train = np.array(x_train, dtype=float)

import tensorflow as tf
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, input_shape=[2], activation='relu'),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(1024, activation='relu'),
    tf.keras.layers.Dense(units=171, activation='softmax')
])


model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
hist = model.fit(x_train, x_label, epochs=50)
from numpy.core.numeric import Inf
import tensorflow as tf
import numpy as np
import random

pred = []
for i in range(132):
    pred.append(random.randint(0,1))

pred = np.array(pred, dtype=float)
pred = pred.reshape(1, 132)

with open('./Model/model.json', 'r') as f:
    model_json = f.read()
model = tf.keras.models.model_from_json(model_json)
model.load_weights('./Model/model.h5')

res = model.predict(pred)
max = -Inf
result = []
for r in res[0]:
    result.append(r)
    if max < r:
        max = r

with open('./processedData/DiseaseLabel.csv', 'r') as f:
    f.readline()
    for row in f.readlines():
        row = row.strip('\n').split(',')
        if int(row[0]) == result.index(max):
            print(row[1])
            break
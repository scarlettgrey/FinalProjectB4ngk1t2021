trainData = []
trainLabel = []
with open('./processedData/Training.csv') as f:
    f.readline()
    for row in f.readlines():
        row = row.strip('\n').split(',')
        trainData.append(row[:-1])
        trainLabel.append(row[len(row) - 1])

testData = []
testLabel = []
with open('./processedData/Testing.csv') as f:
    f.readline()
    for row in f.readlines():
        row = row.strip('\n').split(',')
        testData.append(row[:-1])
        testLabel.append(row[len(row) - 1])

for a in range(len(trainData)):
    for b in range(len(trainData[a])):
        trainData[a][b] = float(trainData[a][b])

for a in range(len(testData)):
    for b in range(len(testData[a])):
        testData[a][b] = float(testData[a][b])

for a in range(len(trainLabel)):
    trainLabel[a] = float(trainLabel[a])

for a in range(len(testLabel)):
    testLabel[a] = float(testLabel[a])

from numpy import random
import tensorflow as tf
from tensorflow.keras import models
from tensorflow.keras.optimizers import SGD, RMSprop
import numpy as np

trainData = np.array(trainData, dtype=float)
trainLabel = np.array(trainLabel, dtype=float)
testData = np.array(testData, dtype=float)
testLabel = np.array(testLabel, dtype=float)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(192, input_shape=[len(trainData[0])], activation='relu'),
    tf.keras.layers.Dense(384, activation='relu'),
    tf.keras.layers.Dense(42, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer=RMSprop(lr=0.05, momentum=0.88), metrics=['accuracy'])
model.fit(trainData, trainLabel, validation_data=(testData, testLabel), epochs=50)

# Save model weight
model_json = model.to_json()
with open('./Model/model.json', 'w') as f:
    f.write(model_json)
model.save_weights('./Model/model.h5')

# Save model
# model.save('./Model/model.h5')

# import random
# pred = []
# for i in range(132):
#     pred.append(random.randint(0,1))
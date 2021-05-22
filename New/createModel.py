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

import tensorflow as tf
import numpy as np

trainData = np.array(trainData, dtype=float)
trainLabel = np.array(trainLabel, dtype=float)
testData = np.array(testData, dtype=float)
testLabel = np.array(testLabel, dtype=float)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(192, input_shape=[len(trainData[0])], activation='relu'),
    tf.keras.layers.Dense(384, activation='relu'),
    tf.keras.layers.Dense(41, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(trainData, trainLabel, validation_data=(testData, testLabel), epochs=50)
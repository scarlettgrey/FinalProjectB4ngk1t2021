trainData = []
trainTemp = []
with open('./processedData/Training.csv') as f:
    f.readline()
    for row in f.readlines():
        row = row.strip('\n').split(',')
        trainData.append(row[:-1])
        trainTemp.append(int(row[len(row) - 1]))

trainLabel = []
for a in trainTemp:
    temp = []
    for i in range(41):
        temp.append(1 if a == i + 1 else 0)
    trainLabel.append(temp)

testData = []
testTemp = []
with open('./processedData/Testing.csv') as f:
    f.readline()
    for row in f.readlines():
        row = row.strip('\n').split(',')
        testData.append(row[:-1])
        testTemp.append(int(row[len(row) - 1]))

testLabel = []
for a in testTemp:
    temp = []
    for i in range(41):
        temp.append(1 if a == i + 1 else 0)
    testLabel.append(temp)

import numpy as np

trainData = np.array(trainData, dtype=float)
trainLabel = np.array(trainLabel, dtype=float)
testData = np.array(testData, dtype=float)
testLabel = np.array(testLabel, dtype=float)

import tensorflow as tf
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(62, input_shape=[len(trainData[0])], activation='relu'),
    tf.keras.layers.Dense(100, activation='selu'),
    tf.keras.layers.Dense(100, activation='relu'),
    tf.keras.layers.Dense(100, activation='relu'),
    tf.keras.layers.Dense(41, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['Recall', 'Precision', 'accuracy'])
history = model.fit(trainData, trainLabel, validation_data=(testData, testLabel), epochs=50, verbose=1)

f = open('./processedData/DiseaseLabel.csv', 'r')
f.readline()
rows = f.readlines()
f.close()
result = []
for i in range(len(testData)):
    res = model.predict(np.array(testData[i]).reshape(1, 132))
    max = -999
    temp = []
    for r in res[0]:
        temp.append(r)
        if max < r:
            max = r
    for row in rows:
        row = row.strip('\n').split(',')
        if int(row[0]) == temp.index(max) + 1:
            result.append(int(row[0]))
            break

conf_matrix = tf.math.confusion_matrix(labels=testTemp, predictions=result)
print("Confunsions Matrix")
print(len(conf_matrix), 'X', len(conf_matrix[0]))
for i in conf_matrix:
    for j in i:
        print(j.numpy(), end=" ")
    print()

# Save model weight
# model_json = model.to_json()
# with open('./Model/model.json', 'w') as f:
#     f.write(model_json)
# model.save_weights('./Model/model.h5')

# Save model
# tf.keras.Model.save(model, './Model')

# Save Pickle Model
# import pickle
# weight = model.get_weights()
# pkl = './Pkl/model.pkl'
# with open(pkl, 'wb') as f:
#     pickle.dump(weight, f, protocol=pickle.HIGHEST_PROTOCOL)

# import random
# pred = []
# for i in range(132):
#     pred.append(random.randint(0,1))

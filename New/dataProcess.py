trainData = []
trainLabel = []
with open('./SrcData/Training.csv', 'r') as f:
    label = f.readline().strip('\n')
    for row in f.readlines():
        row = row.strip('\n').split(',')[:-1]
        trainData.append(row[:-1])
        trainLabel.append(row[len(row) - 1])

testData = []
testLabel = []
with open('./SrcData/Testing.csv') as f:
    f.readline()
    for row in f.readlines():
        row = row.strip('\n').split(',')
        testData.append(row[:-1])
        testLabel.append(row[len(row) - 1])

encoder = {}
e = 1
for dis in trainLabel:
    append = True
    for enc in encoder:
        if encoder[enc] == dis:
            append = False
            break
    if append == True:
        encoder[e] = dis
        e += 1

with open('./processedData/DiseaseLabel.csv', 'w') as f:
    f.write('label,diseasen_name')
    for enc in encoder:
        f.write('\n' + str(enc) + ',' + encoder[enc])

with open('./processedData/Training.csv', 'w') as f:
    f.write(label)
    for A, b in zip(trainData, trainLabel):
        f.write('\n')
        for a in A:
            f.write(a + ',')
        for enc in encoder:
            if encoder[enc] == b:
                f.write(str(enc))
                break

with open('./processedData/Testing.csv', 'w') as f:
    f.write(label)
    for A, b in zip(testData, testLabel):
        f.write('\n')
        for a in A:
            f.write(a + ',')
        for enc in encoder:
            if encoder[enc] == b:
                f.write(str(enc))
                break
import pandas as pd 
import matplotlib.pyplot as plt

randloc = pd.read_csv('./RandLoc/' + 'RandomLongLat0.csv')
randloc = randloc.iloc[::, :].copy()

dataset = pd.read_csv('Outputs-rev.csv')
dataset = dataset.iloc[::, :].copy()

print(len(randloc))
print(len(dataset))

plt.scatter(x = randloc['Long'], y=  randloc['Lat'])
plt.scatter(x = dataset['Long'], y=  dataset['Lat'])
plt.scatter(x = randloc['Long'][0], y=  randloc['Lat'][0]) #check random position
plt.scatter(x = dataset['Long'][43], y=  dataset['Lat'][43]) #check recomended nearest hospital (with available room and doctor)
plt.legend(['random', 'data', 'point', 'rec'])
plt.show()
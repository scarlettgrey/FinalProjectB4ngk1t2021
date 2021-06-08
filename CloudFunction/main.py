import requests
from google.cloud import storage
import numpy as np
import tensorflow as tf
import os
import json

os.mkdir('/tmp/Model')
os.mkdir('/tmp/Model/variables')

storage = storage.Client()
bucket = storage.get_bucket('model_ai_v1') # Change to your bucket name
blob = bucket.blob('')
blobname = [blob.name for blob in bucket.list_blobs()]
blob = bucket.blob(blobname[1])
blob.download_to_filename('/tmp/Model/saved_model.pb')
vardata = bucket.blob(blobname[2])
vardata.download_to_filename('/tmp/Model/variables/variables.data-00000-of-00001')
varindex = bucket.blob(blobname[3])
varindex.download_to_filename('/tmp/Model/variables/variables.index')
model = tf.keras.models.load_model('/tmp/Model')
label = bucket.blob(blobname[0])
label.download_to_filename('/tmp/DiseaseLabel.csv')
label = '/tmp/DiseaseLabel.csv'
f = open(label, 'r')
f.readline()
rows = []
for row in f.readlines():
    rows.append(row.strip('\n').split(','))
f.close()

def api_pred(request):
    if request.method == 'GET':
        return "Bad Request"
    elif request.method == 'POST':
        data = request.get_json()
        try:
            data = np.array(data['symptoms'], dtype=float)
            data = data.reshape(1, 132)
        except:
            d = []
            for a in data['symptoms']:
                try:
                    d.append(int(a))
                except:
                    pass
            data = np.array(d, dtype=float)
            data = data.reshape(1, 132)
        pred = model.predict(data)

        Max = -999
        result = []
        for p in pred[0]:
            result.append(p)
            if Max < p:
                Max = p
        results = {}
        for row in rows:
            if int(row[0]) == result.index(Max) + 1:
                results['disease'] = row[1]
        return json.dumps(results)

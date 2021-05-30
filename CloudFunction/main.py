import requests
from google.cloud import storage
import numpy as np
import tensorflow as tf
import os

os.mkdir('/tmp/Model')
os.mkdir('/tmp/Model/variables')

storage = storage.Client()
bucket = storage.get_bucket('model_ai_v1')
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

def api_pred(request):
    if request.method == 'GET':
        return 'GET AWAY'
    elif request.method == 'POST':
        data = request.get_json()
        data = np.array(data['symptoms'], dtype=float)
        data = data.reshape(1, 132)
        pred = model.predict(data)

        Max = -999
        result = []
        for p in pred[0]:
            result.append(p)
            if Max < p:
                Max = p

        with open(label, 'r') as f:
            f.readline()
            for row in f.readlines():
                row = row.strip('\n').split(',')
                if int(row[0]) == result.index(Max):
                    return row[1]
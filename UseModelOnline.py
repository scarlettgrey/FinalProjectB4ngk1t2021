import requests
import random

url = 'https://asia-southeast2-rational-logic-308203.cloudfunctions.net/model-caller-py'
param = {
    "symptoms" : [random.randint(0, 1) for a in range(132)]
}

sess = requests.session()
res = sess.post(url, json=param)
print("Based on my prediction You may have {}".format(res.text))
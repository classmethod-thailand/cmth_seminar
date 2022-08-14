import requests
import json
import datetime
import random
import math

# parameter
endpoint = 'ahakc63geq1k5-ats.iot.ap-southeast-1.amazonaws.com'
topic = "test/keisuke-20220813"
cert = "604ca25501f352ba6f9a019d0f7b97614c0555d67abbeb0ba99ae3bb12ce204a-certificate.pem.crt"
key = "604ca25501f352ba6f9a019d0f7b97614c0555d67abbeb0ba99ae3bb12ce204a-private.pem.key"

# create request data
hour = datetime.datetime.now().hour
a1 = math.sin(hour * math.pi / 24) + 1
dist = random.lognormvariate(a1, a1 / 3)
if dist <= 0.1:
    dist = 0.1
json_obj = {
    "distance": dist,
    "datetime": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
}
message = json.dumps(json_obj)

publish_url = 'https://' + endpoint + ':8443/topics/' + topic + '?qos=1'
publish_msg = message.encode('utf-8')

# make request
publish = requests.request('POST', publish_url, data=publish_msg, cert=[cert, key])

# print results
print("Response status: ", str(publish.status_code))
if publish.status_code == 200:
    print("Response body:", publish.text)

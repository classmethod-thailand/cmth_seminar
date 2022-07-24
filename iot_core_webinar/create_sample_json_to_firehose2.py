import json
import datetime
import random
import math
import boto3

firehose_stream_name = "keisuke-test-2"

hour = datetime.datetime.now().hour
a1 = math.sin(hour * math.pi / 24) + 1
dist = random.lognormvariate(a1, a1 / 3)
if dist <= 0.1:
    dist = 0.1

json_obj = {
    "timestamp": datetime.datetime.now().timestamp(),
    "payloads":{
        "distance": dist,
    }
}
send_data = (json.dumps(json_obj) + "\n").encode()

client = boto3.client('firehose', region_name='ap-southeast-1')
response = client.put_record(
    DeliveryStreamName = firehose_stream_name,
    Record = {"Data": send_data})

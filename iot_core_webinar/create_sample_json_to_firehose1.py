import json
import datetime
import random
import math
import boto3

firehose_stream_name = "keisuke-test"

hour = datetime.datetime.now().hour
a1 = math.sin(hour * math.pi / 24) + 1
dist = random.lognormvariate(a1, a1 / 3)
if dist <= 0.1:
    dist = 0.1

json_obj = {
    "distance": dist,
    "datetime": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
}
send_data = (json.dumps(json_obj) + "\n").encode()

client = boto3.client('firehose', region_name='ap-southeast-1')
response = client.put_record(
    DeliveryStreamName = firehose_stream_name,
    Record = {"Data": send_data})

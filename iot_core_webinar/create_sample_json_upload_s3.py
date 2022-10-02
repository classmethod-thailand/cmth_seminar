import subprocess
import json
import datetime
import time
import random
import math

s3_bucket_name = "keisuke-test-20220607"

s3_path = "json" + datetime.datetime.now().strftime('%Y%m%d')
file_name = datetime.datetime.now().strftime('%Y%m%d_%H%M%S.json')

hour = datetime.datetime.now().hour
a1 = math.sin(hour * math.pi / 24) + 1
dist = random.lognormvariate(a1, a1 / 3)
if dist <= 0.1:
    dist = 0.1

json_obj = {
    "distance": dist,
    "device": random.randint(1, 3),
    "datetime": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
}

with open(file_name, 'w') as f:
    json.dump(json_obj, f, ensure_ascii=False)

subprocess.run(["/usr/bin/aws", "s3", "cp", file_name, f"s3://{s3_bucket_name}/{s3_path}/"])

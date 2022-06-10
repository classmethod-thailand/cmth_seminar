import subprocess
import json
import datetime
import time
import random
import math

s3_bucket_name = "keisuke-test-20220607"

s3_path = datetime.datetime.now().strftime('%Y%m%d')
file_name = datetime.datetime.now().strftime('%Y%m%d_%H%M%S.json')

a1 = math.sin(datetime.datetime.now().hour * math.pi * 2 / 2 / 240)
dist = random.lognormvariate(a1, a1 / 2)
if dist <= 0.1:
  dist = 0.1

json_obj = {
    "distance": dist,
    "datetime": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
}

with open(file_name, 'w') as f:
    json.dump(json_obj, f, ensure_ascii=False)

subprocess.run(["/usr/bin/aws", "s3", "cp", file_name, f"s3://{s3_bucket_name}/{s3_path}/"])

import json
import base64
import datetime

def lambda_handler(event, context):
    results = []
    records = event["records"]
    for record in records:
        # read record
        recordId = record["recordId"]
        decoded_data = base64.b64decode(record["data"])
        payload = json.loads(decoded_data)
        print("payload: " + str(payload))

        # transform record
        transformed_payload = {
            "datetime": datetime.datetime.fromtimestamp(payload['timestamp']).strftime('%Y-%m-%d %H:%M:%S'),
            "distance": payload['payloads']['distance'],
        }
        print("transformed_payload: " + str(transformed_payload))

        # write record
        decoded_data = json.dumps(transformed_payload) + '\n'
        data = base64.b64encode(decoded_data.encode())

        results.append({
            "result": "Ok",
            "recordId": recordId,
            "data": data,
        })
    return {
        "records": results
    }

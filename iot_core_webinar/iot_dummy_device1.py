from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
import json
import datetime
import random
import math

# Setting
ENDPOINT = "ahakc63geq1k5-ats.iot.ap-southeast-1.amazonaws.com"
CLIENT_ID = "keisuke-20220724"
PATH_TO_CERTIFICATE = "ee8b89b90d3a8772962f2be0c1f9a2e5bb2eec6e2db50b233791bcc4ca87cc65-certificate.pem.crt"
PATH_TO_PRIVATE_KEY = "ee8b89b90d3a8772962f2be0c1f9a2e5bb2eec6e2db50b233791bcc4ca87cc65-private.pem.key"
PATH_TO_AMAZON_ROOT_CA_1 = "AmazonRootCA1.pem"
TOPIC = "test/" + CLIENT_ID

# Initialize resources
event_loop_group = io.EventLoopGroup(1)
host_resolver = io.DefaultHostResolver(event_loop_group)
client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint         = ENDPOINT,
    cert_filepath    = PATH_TO_CERTIFICATE,
    pri_key_filepath = PATH_TO_PRIVATE_KEY,
    client_bootstrap = client_bootstrap,
    ca_filepath      = PATH_TO_AMAZON_ROOT_CA_1,
    client_id        = CLIENT_ID,
    clean_session    = False,
    keep_alive_secs  = 6
)
print("Connecting to {} with client ID '{}'...".format(
    ENDPOINT, CLIENT_ID))
# Make the connect() call
connect_future = mqtt_connection.connect()
# Future.result() waits until a result is available
connect_future.result()
print("Connected!")

# Publish message to server desired number of times.
print('Begin Publish')

hour = datetime.datetime.now().hour
a1 = math.sin(hour * math.pi / 24) + 1
dist = random.lognormvariate(a1, a1 / 3)
if dist <= 0.1:
    dist = 0.1

json_obj = {
    "distance": dist,
    "datetime": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
}

mqtt_connection.publish(topic = TOPIC, payload = json.dumps(json_obj), qos = mqtt.QoS.AT_LEAST_ONCE)
print("Published: '" + json.dumps(json_obj) + "' to the topic: " + TOPIC)

# Disconnect
print('Begin Disconnect')
disconnect_future = mqtt_connection.disconnect()
disconnect_future.result()


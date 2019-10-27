import paho.mqtt.client as mqtt
import time
import random

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

client = mqtt.Client()
client.on_publish = on_publish
client.connect("127.0.0.1", 1883)
client.loop_start()

while True:
    pH = random.uniform(5,11)
    client.publish("/sensor/air", str(pH), qos=1)
    time.sleep(10)

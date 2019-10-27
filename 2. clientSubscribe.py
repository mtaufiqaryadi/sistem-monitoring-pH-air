import paho.mqtt.client as mqtt
import simplejson
import http.client, urllib

conn = http.client.HTTPConnection("localhost:9998")

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def semua():
    conn.request("GET", "/ph")
    response = conn.getresponse()
    resp = response.read()
    data = simplejson.loads(resp)
    for m in data :
        print(m['ph'])

def on_message(client, userdata, msg):
    print(msg.topic+" "+" "+str(msg.payload))
    #semua()
    phbaru = str(msg.payload)
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    params = urllib.parse.urlencode({'ph':phbaru})
    conn.request("POST", "/ph", params, headers)
    response = conn.getresponse()

            
client = mqtt.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("127.0.0.1", 1883)
client.subscribe("/sensor/air", qos=1)

client.loop_forever()


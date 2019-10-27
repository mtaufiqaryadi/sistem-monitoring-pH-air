import http.client, urllib
import simplejson

conn = http.client.HTTPConnection("localhost:9998")

def semua():
    conn.request("GET", "/ph")
    response = conn.getresponse()
    resp = response.read()
    data = simplejson.loads(resp)
    for m in data :
        print(m['ph'])
        
semua()

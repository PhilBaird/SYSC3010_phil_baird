import http.client
import urllib.parse
import time
key = "AT68QYQ94MQEWXL3"
#key = "JXB39Y73FYFB1Y4K"
def write():
    while True:
        params = urllib.parse.urlencode({'field1': "L3-t-6", 'field2': "philipbaird@cmail.carleton.ca", 'field3': "b",'key':key })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        break
if __name__ == "__main__":
    write()
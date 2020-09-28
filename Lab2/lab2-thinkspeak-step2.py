import requests


def read():
    URL = 'https://api.thingspeak.com/channels/1161282/fields/1.json?api_key='
    KEY = 'F2Q2UUQ0HDTLMK25'
    HEADER = '&results=20'
    NEW_URL = URL + KEY + HEADER
    try:
        data = requests.get(NEW_URL).json()
        # print(data)
        id = data['channel']['id']
        field = data['feeds']
        print(field)
    except:
        print("connection failed")


if __name__ == "__main__":
    read()
import requests
import time


# import json

# api_url = "https://jsonplaceholder.typicode.com/todos/1"

def getipaddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipaddress = s.getsockname()[0]
    s.close()
    return ipaddress


def main():
    while True:
        ipaddress = getipaddress()
        print("test:" + str(ipaddress) + " " + str(datetime.datetime.now()))
        response = requests.get(ipaddress + "/status")  # api_url)
        print(response.json())
        data = response.json()  # json.load(response.json())#need to test this piece
        time.sleep(10)


main()

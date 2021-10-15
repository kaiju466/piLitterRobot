import requests
import time
import socket
import os
import datetime

# import json

# api_url = "https://jsonplaceholder.typicode.com/todos/1"

cycle_count = 1
cycle_num_max = 4

current_datetime = datetime.date.today()

next_run_datetime = datetime.datetime(2021, 7, 12, 9, 55, 0, 342380)
next_song_run = datetime.datetime(2021, 7, 12, 9, 55, 0, 342380)

curDir = 0 # -1=reverse,0=stopped,1=forward
curPos = 0  # Unknown=-1,Home=0,Dump=1
curDest = 0  # Unknown=-1,Home=0,Dump=1

numInterval_Hours = 10
dump_time = 20  # in secs

flaskSFlag=True
mainSFlag=True

def getipaddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipaddress = s.getsockname()[0]
    s.close()
    return ipaddress

def apiGet(ip_address):
    response = requests.get("http://"+ip_address + ":5000/status")  # api_url)
    print(response.json())
    data = response.json()  # json.load(response.json())#need to test this piece
    print(str(data["destination"]))
    print(str(data["direction"]))
    print(str(data["nexttime"]))
    print(str(data["hoursbtwnruns"]))
    print(str(data["eStop"]))
    if data["eStop"]==True:
        print("Emergency Stop!!")
        quit()

def apiPut(ip_address):
    templateData = {
        'direction': curDir,
        'destination': curDest,
        'nexttime': str(next_run_datetime),
        'hoursbtwnruns': numInterval_Hours,
        'eStop': False
    }
    
    response = requests.post("http://"+ip_address + ":5000/status", json=templateData)
    response.json()

def main():
    while True:
        ipaddress = getipaddress()
        print("test:" + str(ipaddress) + " " + str(datetime.datetime.now()))
        apiGet(ipaddress)
        time.sleep(10)
        apiPut(ipaddress)
        time.sleep(10)
        apiGet(ipaddress)
        
def main2():
    #while True:
    ipaddress = getipaddress()
    print("test:" + str(ipaddress) + " " + str(datetime.datetime.now()))
    apiGet(ipaddress)
    time.sleep(10)
    apiPut(ipaddress)
    time.sleep(10)
    apiGet(ipaddress)
    

main()

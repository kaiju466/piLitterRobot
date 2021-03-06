
from flask import Flask, render_template
from multiprocessing import Process, Value

import datetime
import socket
import os


app = Flask(__name__)

#plan for website interface
#piLitterBox Portal
#Cycle now button
#current status
#  current position
#  Current direction/motor direction
#  Current Destination
#  Graphic of position?
#  Next Run time
#  Number of Runs
#  Hours between runs
#  Eventual schedule mechanic?
#  Eventual fill level when hardware is added
#Email recipients
#Android app?



#variables
prog_version = 1.0
prog_name = "Flask Hello Test Program 1"
#mode = GPIO.getmode()
cycle_count=1
cycle_num_max=4

current_datetime=datetime.date.today()

next_run_datetime=datetime.datetime(2021, 7, 12, 9, 55, 0, 342380)
next_song_run=datetime.datetime(2021, 7, 12, 9, 55, 0, 342380)

curDir=0#-1=reverse,0=stopped,1=forward
curPos=-1#Unknown=-1,Home=0,Dump=1
curDest=-1#Unknown=-1,Home=0,Dump=1

numInterval_Hours=6
dump_time=20#in secs

logname = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'litterbox_main.log')

places = {
        0: 'home',
        1: 'dump',
        -1: 'Unknown'
}
direction = {
        0: 'stopped',
        1: 'forward',
        -1: 'reverse'
}


#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

#methods and functions here
@app.route("/")#use this to designate function that page will go to on root
def index():
    global curPos, lastDir, curDir, curDest, next_run_datetime,places,direction
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    f = open(logname, "r")
    print(str(direction[curDir]))
    
    templateData = {
        'direction': str(direction[curDir]),
        'time': timeString,
        'destination': str(places[curDest]),
        'nexttime': str(next_run_datetime),
        'hoursbtwnruns': str(numInterval_Hours),
        'msglog': f.read()
    }
    print(templateData)
    return render_template('index.html', **templateData)

@app.route("/hello")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
   print(templateData)
   return render_template('index.html', **templateData)

@app.route("/hello2")
def hello2():
    print("Hello")
    return 'Hello world'

@app.route("/emergencystop",methods=['POST','GET'])
def emergencystop():
    global curPos, lastDir, curDir, curDest, next_run_datetime,places,direction
    logAndPrint(logging.info,"Emergency Stop!!")
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    f = open(logname, "r")

    templateData = {
        'direction': str(direction[curDir]),
        'time': timeString,
        'destination': str(places[curDest]),
        'nexttime': str(next_run_datetime),
        'hoursbtwnruns': str(numInterval_Hours),
        'msglog': f.read()
    }
    print(templateData)
    return render_template('index.html', **templateData)

@app.route("/manualrun",methods=['POST','GET'])
def manualrun():
    global curPos, lastDir, curDir, curDest, next_run_datetime,places,direction
    logAndPrint(logging.info,"Manual Run")
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    f = open(logname, "r")
    
    templateData = {
        'direction': str(direction[curDir]),
        'time': timeString,
        'destination': str(places[curDest]),
        'nexttime': str(next_run_datetime),
        'hoursbtwnruns': str(numInterval_Hours),
        'msglog': f.read()
    }
    print(templateData)
    return render_template('index.html', **templateData)

def getipaddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipaddress=s.getsockname()[0]
    s.close()
    return ipaddress

def main():
    while True:
        print("test:"+str(datetime.datetime.now()))

# Title Screen
print("---------------------------------")
print("-" + prog_name + " " + str(prog_version) + "  -")
#print("-Date:" + current_datetime.today().strftime('%Y-%h-%d') + "               -")
print("---------------------------------")
#time.sleep(2.00)
print("Start Test")

ipaddress=getipaddress()

#while True:
#    print("test")
    
#start test code here
#if __name__ == "__main__":
#    app.run(host=ipaddress, port=5000, debug=True)
   #app.run(host='192.168.1.131', port=5000, debug=True)

if __name__ == "__main__":
    Process(target=app.run, kwargs=dict(host=ipaddress, port=5000)).start()
    Process(target=main).start()
    print("Post flask")
   #p = Process(target=main, args=())
   #p.start()  
   #app.run(host=ipaddress, port=5000, debug=True, use_reloader=False)
   #p.join()
   

#Process(target=app.run, kwargs=dict(host='0.0.0.0', port=8080)).start()
#Process(target=statupdate).start()

print("Exiting Test- Goodbye!")



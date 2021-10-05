
from flask import Flask, render_template

import datetime
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
current_datetime=datetime.date.today()
next_run_datetime=datetime.datetime(2021, 7, 12, 9, 55, 0, 342380)

#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

#methods and functions here
@app.route("/")#use this to designate function that page will go to on root
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'direction': 'Unknown1',
        'time': timeString,
        'destination':'Unknown2',
        'nexttime':'Unknown3',
        'hoursbtwnruns':'Unknown4',
        'msglog':'Log goes here'
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
    print("emergencystop")
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'direction': 'Unknown1',
        'time': timeString,
        'destination':'Unknown2',
        'nexttime':'Unknown3',
        'hoursbtwnruns':'Unknown4',
        'msglog':'emergencystop'
    }
    print(templateData)
    return render_template('index.html', **templateData)

@app.route("/manualrun",methods=['POST','GET'])
def manualrun():
    print("manualrun")
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'direction': 'Unknown1',
        'time': timeString,
        'destination':'Unknown2',
        'nexttime':'Unknown3',
        'hoursbtwnruns':'Unknown4',
        'msglog':'manualrun'
    }
    print(templateData)
    return render_template('index.html', **templateData)

# Title Screen
print("---------------------------------")
print("-" + prog_name + " " + str(prog_version) + "  -")
#print("-Date:" + current_datetime.today().strftime('%Y-%h-%d') + "               -")
print("---------------------------------")
#time.sleep(2.00)
print("Start Test")


#start test code here
if __name__ == "__main__":
   app.run(host='192.168.1.131', port=5000, debug=True)


print("Exiting Test- Goodbye!")



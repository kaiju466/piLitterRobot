#!/usr/bin/python
from flask import Flask, render_template
import datetime
app = Flask(__name__)




#variables
prog_version = 1.0
prog_name = "Flask Hello Test Program"
mode = GPIO.getmode()
current_datetime=datetime.date.today()
next_run_datetime=datetime.datetime(2021, 7, 12, 9, 55, 0, 342380)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#methods and functions here
@app.route("/")#use this to designate function that page will go to
def index():
    return 'Hello world'

def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
   return render_template('index.html', **templateData)



# Title Screen
print("---------------------------------")
print("-" + prog_name + " " + str(prog_version) + "  -")
#print("-Date:" + current_datetime.today().strftime('%Y-%h-%d') + "               -")
print("---------------------------------")
time.sleep(2.00)
print("Start Test")


#start test code here
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)


print("Exiting Test- Goodbye!")



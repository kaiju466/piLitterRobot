#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

import time
import atexit
import RPi.GPIO as GPIO
import datetime

prog_version=1.2
prog_name="Custom Pi-Litterbox Robot"
mode = GPIO.getmode()

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

GPIO_PIR=27#23#sensor detection for dump hole
GPIO_PIR2=22#sensor detection for Shift Hole

GPIO.setup(GPIO_PIR2, GPIO.IN)#setup Shift hole

counter=1
counter2=1

cycle_count=1
cycle_num_max=4

flag=True
#dflag=True#dump flag
#sflag=False#home flag

current_datetime=datetime.date.today()
#datetime.datetime.now()
next_run_datetime=datetime.datetime(2021, 7, 12, 9, 55, 0, 342380)
#next_run_time=datetime.time(hour = 20, minute = 45, second = 0)
curDir=0#-1=reverse,0=stopped,1=forward
curPos=-1#Unknown=-1,Home=0,Dump=1
curDest=1#Unknown=-1,Home=0,Dump=1

numInterval_Hours=6
dump_time=20#in secs


#datetime.datetime(2020, 5, 17)

# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)

#initialize motor
myMotor = mh.getMotor(2)
motorSpeed=50#250#150
#flagDir1=myMotor.IN1pin
#flagDir2=myMotor.IN2pin
# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    global curDir
    #print("Stop Motors")
    mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)
    time.sleep(1.00)
    curDir=0
    #print("Done")
atexit.register(turnOffMotors)

def reverseCurMotorDir(dir):
    #print("reverseCurMotorDir")
    turnOffMotors()
    #print("Current Direction:"+str(dir))
    if dir==-1:
        motorForward()
    else:
        motorReverse()
    

def motorForward():
    turnOffMotors()
    global curDir
    #print ("Forward! ")
    #myMotor.setSpeed(motorSpeed)
    #print ("\tSpeed up...")
    myMotor.run(Raspi_MotorHAT.FORWARD)
    for i in range(motorSpeed):
        myMotor.setSpeed(i)
        time.sleep(0.01)
    curDir=1
    #print(str(curDir))

def motorReverse():
    turnOffMotors()
    global curDir
    #print ("Reverse! ")
    myMotor.setSpeed(motorSpeed)
    myMotor.run(Raspi_MotorHAT.BACKWARD)
    
    curDir=-1

def motorStop():
    global curDir
    #print ("Slow down...")
    for i in reversed(range(motorSpeed)):
        myMotor.setSpeed(i)
    time.sleep(0.01)

    #print ("Stop")
    myMotor.run(Raspi_MotorHAT.RELEASE)
    curDir=0
    
def move2Home():
    global curDest
    if curPos==1:
        curDest=0
        motorReverse()
    else:
        motorForward()

def move2Dump():
    print("Preparing to Dump")
    global curDest
    #print(str(curPos))
    if curPos==0:
        curDest=1
        motorForward()
    elif curPos==-1:
        motorForward()
    else:
        motorReverse()
    #print("Finished!")
    #print("Next run date/time:"+str(next_run_datetime))
    
#HallEffect Sensor Test
GPIO.setup(GPIO_PIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)
def printDumpDetected(GPIO_PIR):
    global curPos,lastDir
    #print(str(sflag))
    if curDest==1 and curDir==1 and curPos!=1:
        global counter
        curPos=1
        lastDir=curDir
        #print("printDumpDetected "+str(counter)+" "+str(lastDir))
        counter=counter+1
        motorStop()
        print("Reached Dump")
        #print("Stop")
        #time.sleep(20.00)#10.00)
        countDown(dump_time)
        print("Going Home")
        move2Home()
    else:
        if curDest==0 and curDir==1:
            print("Not Stopping at Dump, heading to Home")
        
    #elif
        
    #mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
GPIO.add_event_detect(GPIO_PIR,GPIO.RISING,callback=printDumpDetected)

def printHomeDetected(GPIO_PIR2):
    global curPos,lastDir
    #print(str(sflag))
    if curDest==0 and curDir==-1 and curPos!=0:
        global counter2
        lastDir=curDir
        #print("printHomeDetected "+str(counter2)+" "+str(lastDir))
        counter2=counter2+1
        #motorStop()
        #print("Stop")
        time.sleep(3.00)
        reverseCurMotorDir(lastDir)
        time.sleep(2.00)
        motorStop()
        curPos=0
        print("Reached Home")
    else:
        if curDest==1 and curDir==-1:
            print("Not Stopping at Home, heading to Dump")
        
GPIO.add_event_detect(GPIO_PIR2,GPIO.RISING,callback=printHomeDetected)


def countDown(num):
    print("waiting for "+str(num)+"secs")
    for i in range(num):
        time.sleep(1)
        print(str(i+1))
    

#title screen
print("---------------------------------")
print("-"+prog_name+" "+str(prog_version)+"  -")
print("-Date:"+current_datetime.today().strftime('%Y-%h-%d')+"               -")
print("---------------------------------")

time.sleep(2.00)

#main
while (flag):
    #print("Next run date/time:"+str(next_run_datetime))
    current_datetime=datetime.datetime.now()
    #print("motor direction:"+str(curDir))
    if current_datetime>=next_run_datetime and cycle_count<=cycle_num_max and curDir==0:
        
        if cycle_count>1:
            print("Time to clean the litter!")
            
        print("Current run date/time:"+str(current_datetime))
        #print("motor direction:"+str(curDir))
        next_run_datetime=(datetime.datetime.now() + datetime.timedelta(hours=numInterval_Hours))#minutes=numInterval_Hours))#
        if (cycle_count+1)<=cycle_num_max:
            print("Next run date/time:"+str(next_run_datetime))
        
        if cycle_count==1:
            print("Proceeding to run initial Dump and return to Home calibration!")
            
        move2Dump()
        
    else:
        #print(str(curDir)+" "+str(curPos)+" "+str(curDest)+" "+str(cycle_count)+" "+str(cycle_num_max))
        if curDir==0 and curPos==0 and curDest==0:
            #print(str(cycle_count)+" "+str(cycle_num_max)+str(cycle_count>=cycle_num_max))
            if cycle_count>=cycle_num_max:# and curDir==0 and curPos==0:
                print("Max Number of Cycles Reached:"+str(cycle_num_max))
                flag=false
                time.sleep(60)
            else:
                print("Cycle "+str(cycle_count)+" of "+str(cycle_num_max))
                cycle_count=cycle_count+1
                curDest=-1
            #counter=3minutes=numInterval_Hours))#
            #counter2=3
    #print("Date:"+str(current_datetime.today().strftime('%Y-%m-%d-%H:%M')))
    #print(str(flagDir1)+" "+str(flagDir2))
	
print("Exiting- Goodbye!")

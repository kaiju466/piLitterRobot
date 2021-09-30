#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from gpiozero import Buzzer
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone

import time
import atexit
import RPi.GPIO as GPIO
import datetime
import logging
import os
import configparser
import smtplib, ssl


# Load the Log file
logname = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'litterbox_main.log')
#print(str(logname))
os.remove(logname)
logging.basicConfig(filename=logname, level=logging.DEBUG)#litterbox_main.log

# Load the configuration file
configname= os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Litterbox_main.ini')
config = configparser.ConfigParser()
config.sections()
config.read(configname)



prog_version=1.7


port = config.get("Email", "port")#587  # For starttls
smtp_server = config.get("Email","smtp_server")#"smtp.gmail.com"
sender_email = config.get("Email","SenderEmail")#"piLitterRobot@gmail.com"
receiver_email = config.get("Email","ReceiverEmail")#"kaiju466@gmail.com"
password = config.get("Email","SndPwd")#input("Type your password and press enter:")
subject="Subject:"
context = ssl.create_default_context()


prog_name="Custom Pi-Litterbox Robot"
mode = GPIO.getmode()

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

GPIO_PIR=27#23#sensor detection for Home
GPIO_PIR2=22#sensor detection for Dump

GPIO_Buzzer=26#buzzer pin
b = TonalBuzzer(GPIO_Buzzer)

#GPIO_OverRide=#button used for manual run
#GPIO_STATLIGHT=#led used to indicate finished status and issues# Blick=issue,On=Done,Off=Ok

GPIO.setup(GPIO_PIR2, GPIO.IN)#setup Dump

#counter=1
#counter2=1

cycle_count=1
cycle_num_max=4


flag=True
#dflag=True#dump flag
#sflag=False#home flag

current_datetime=datetime.date.today()
#datetime.datetime.now()
next_run_datetime=datetime.datetime(2021, 7, 12, 9, 55, 0, 342380)
next_song_run=datetime.datetime(2021, 7, 12, 9, 55, 0, 342380)
#next_run_time=datetime.time(hour = 20, minute = 45, second = 0)

curDir=0#-1=reverse,0=stopped,1=forward
curPos=-1#Unknown=-1,Home=0,Dump=1
curDest=1#Unknown=-1,Home=0,Dump=1

numInterval_Hours=6
dump_time=20#in secs

#GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#cb = ButtonHandler(4, real_cb, edge='rising', bouncetime=100)
#cb.start()
#GPIO.add_event_detect(4, GPIO.RISING, callback=cb)

#datetime.datetime(2020, 5, 17)

# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)#default address: 0x6f

#initialize motor
myMotor = mh.getMotor(2)
motorSpeed=50#250#150


# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    global curDir
    #logAndPrint(logging.info,"Stop Motors")
    mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)
    time.sleep(1.00)
    curDir=0
    #logAndPrint(logging.info,"Done")
atexit.register(turnOffMotors)

def reverseCurMotorDir(dir):
    #logAndPrint(logging.info,"reverseCurMotorDir")
    turnOffMotors()
    #logAndPrint(logging.info,"Current Direction:"+str(dir))
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
    #logAndPrint(logging.info,str(curDir))

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

#moves globe to shift waste from litter and dump
def move2Dump():
    logAndPrint(logging.info,"Preparing to Dump")
    global curDest
    #logAndPrint(logging.info,str(curPos))
    if curPos==0:
        curDest=1
        motorForward()
    elif curPos==-1:
        motorForward()
    else:
        motorReverse()
    #logAndPrint(logging.info,"Finished!")
    #logAndPrint(logging.info,"Neimport ConfigParserxt run date/time:"+str(next_run_datetime))
        
#moves globe to completely dump litter
def move2FullDump():
    logAndPrint(logging.info,"Preparing to Full Dump")
    global curDest
    #logAndPrint(logging.info,str(curPos))
    if curPos==0:
        curDest=1
        motorReverse()
    elif curPos==-1:
        motorReverse()
    else:
        motorForward()
    #logAndPrint(logging.info,"Finished!")
    #logAndPrint(logging.info,"Next run date/time:"+str(next_run_datetime))
    
#HallEffect Sensor functions
GPIO.setup(GPIO_PIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)
def printDumpDetected(GPIO_PIR):
    global curPos,lastDir
    #logAndPrint(logging.info,str(sflag))
    if curDest==1 and curDir==1 and curPos!=1:
        #global counter
        curPos=1
        lastDir=curDir
        #logAndPrint(logging.info,"printDumpDetected "+str(counter)+" "+str(lastDir))
        #counter=counter+1
        motorStop()
        logAndPrint(logging.info,"Reached Dump")
        #logAndPrint(logging.info,"Stop")
        #time.sleep(20.00)#10.00)
        countDown(dump_time)
        logAndPrint(logging.info,"Going Home")
        move2Home()
    else:
        if curDest==0 and curDir==1:
            logAndPrint(logging.info,"Not Stopping at Dump, heading to Home")
        
    #elif
        
    #mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
GPIO.add_event_detect(GPIO_PIR,GPIO.RISING,callback=printDumpDetected)

def printHomeDetected(GPIO_PIR2):
    global curPos,lastDir
    #logAndPrint(logging.info,str(sflag))
    if curDest==0 and curDir==-1 and curPos!=0:
        #global counter2
        lastDir=curDir
        #logAndPrint(logging.info,"printHomeDetected "+str(counter2)+" "+str(lastDir))
        #counter2=counter2+1
        #motorStop()
        #logAndPrint(logging.info,"Stop")
        time.sleep(scaleTiming(5.00,motorSpeed))#time.sleep(3.00)
        reverseCurMotorDir(lastDir)
        time.sleep(scaleTiming(4.00,motorSpeed))#time.sleep(2.00)
        motorStop()
        curPos=0
        logAndPrint(logging.info,"Reached Home")
    else:
        if curDest==1 and curDir==-1:
            logAndPrint(logging.info,"Not Stopping at Home, heading to Dump")
        
GPIO.add_event_detect(GPIO_PIR2,GPIO.RISING,callback=printHomeDetected)

#Manual Interaction Functions
#def manualOverride:
#    logAndPrint(logging.info,"Manual Override Detected")
#    logAndPrint(logging.info,"Run Cycle")
#    cycle_num_max=cycle_num_max+1
#    next_run_datetime=datetime.datetime.now()

#GPIO.add_event_detect(GPIO_OverRide,GPIO.RISING,callback=manualOverride)

#code for enabling ircontrol of box
#def irOverride:
#    logAndPrint(logging.info,"IR Override Detected")

#Misc functions
def countDown(num):
    logAndPrint(logging.info,"waiting for "+str(num)+"secs")
    for i in range(num):
        time.sleep(1)
        logAndPrint(logging.info,str(i+1)+ " Mississippi")

def scaleTiming(time,speed):
    ##speed range 1-255 (units=?)
    ##speed=0 is stopped
    maxSpeed=255
    minSpeed=1
    logAndPrint(logging.info,"Scale "+str(time)+" Seconds for "+str(speed)+" Speed")
    logAndPrint(logging.info,"Percentage Max speed is "+str((speed/maxSpeed)*100))
    return (time*(maxSpeed/speed))#reverse scales percentage to get time delay based on speed

#music functions
#Note range A3-G5
def playtone(frequency):
    b.play(Tone(frequency))
    time.sleep(0.5)
    b.stop()

def finishSong():
    song = ["A4","P","B4","C4"]
    song=song[::-1]
    playsong(song)

def troubleSong():
    song = ["A3","A4","A5"]
    song=song[::-1]
    playsong(song)

def startupSong():
    song = ["A4","P","B4","C4"]
    playsong(song)

def ode2JoySong():
    song = ["C4","C4","D4","E4","P","E4","D4","C4","B3","P","B3","B3","C4","D4"]
    playsong(song)

    
def playsong(mysong):
    #logAndPrint(logging.info,str(len(mysong)))
    for i in range(len(mysong)):
        if (mysong[i] == "P"):
            time.sleep(0.25)
        else:
            playtone(mysong[i])

#email function
def notify(sbj,msg):
    try:
        logAndPrint(logging.debug,"start email process")
        with smtplib.SMTP(smtp_server, port) as server:
            logAndPrint(logging.debug,"start email server")
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            sbj=subject+sbj
            server.sendmail(sender_email, receiver_email, sbj+" \n"+msg)
            logAndPrint(logging.debug,"End email")
    except Exception as err:
        logAndPrint(logging.error,"Fatal error in notify|"+err.message)
        #logger.exception("Fatal error in notify")

#play song every # min 
def playSongOnRepeat(time,methodToRun):
    global current_datetime,next_song_run
    while (True):
        #next_song_run
        current_datetime=datetime.datetime.now()
        if current_datetime>=next_song_run:
            logAndPrint(logging.info,"Playing Song every "+str(time)+" minute(s)")
            methodToRun()
            next_song_run=(datetime.datetime.now() + datetime.timedelta(minutes=time))#minutes=numInterval_Hours))#
            logAndPrint(logging.info,"Playing next song at "+str(next_song_run))

#console prints messages and logs them to the log file
#def logAndPrint(msgType,msg):
#    #current_datetime=datetime.datetime.now()#.today().strftime('%Y-%h-%d')
#    message=str(current_datetime)+"|"+msg
#    print(message)
#    if msgType=="Debug":
#        logging.debug(message)
#    elif msgType=="Info":
#        logging.info(message)
#   elif msgType=="Warning":
#        logging.warning(message)
#    elif msgType=='Error':
#        logging.error(message)
#    else:
#        logging.error(message)

#console prints messages and logs them to the log file
def logAndPrint(msgMethodType,msg):
    #current_datetime=datetime.datetime.now()#.today().strftime('%Y-%h-%d')
    message=str(current_datetime)+"|"+msg
    print(message)
    msgMethodType(message)


#Title Screen
logAndPrint(logging.info,"---------------------------------")
logAndPrint(logging.info,"-"+prog_name+" "+str(prog_version)+"  -")
logAndPrint(logging.info,"-Date:"+current_datetime.today().strftime('%Y-%h-%d')+"               -")
logAndPrint(logging.info,"---------------------------------")
startupSong()
notify("Starting piLitterRobot","piLitterRobot has started it's run cycle. Will cycle "+str(cycle_num_max)+" times every "+str(numInterval_Hours)+" hours")

time.sleep(2.00)

#main
while (flag):
    #logAndPrint(logging.info,"Next run date/time:"+str(next_run_datetime))
    current_datetime=datetime.datetime.now()
    #logAndPrint(logging.info,"motor direction:"+str(curDir))
    if current_datetime>=next_run_datetime and cycle_count<=cycle_num_max and curDir==0:
        
        if cycle_count>1:
            logAndPrint(logging.info,"Time to clean the litter!")#logAndPrint(logging.info,"Time to clean the litter!")
            
        logAndPrint(logging.info,"Current run date/time:"+str(current_datetime))
        #logAndPrint(logging.info,"motor direction:"+str(curDir))
        next_run_datetime=(datetime.datetime.now() + datetime.timedelta(hours=numInterval_Hours))#minutes=numInterval_Hours))#
        if (cycle_count+1)<=cycle_num_max:
            logAndPrint(logging.info,"Next run date/time:"+str(next_run_datetime))
        
        if cycle_count==1:
            logAndPrint(logging.info,"Proceeding to run initial Dump and return to Home calibration!")
            
        move2Dump()
        
    else:
        #logAndPrint(logging.info,str(curDir)+" "+str(curPos)+" "+str(curDest)+" "+str(cycle_count)+" "+str(cycle_num_max))
        if curDir==0 and curPos==0 and curDest==0:
            #logAndPrint(logging.info,str(cycle_count)+" "+str(cycle_num_max)+str(cycle_count>=cycle_num_max))
            if cycle_count>=cycle_num_max:# and curDir==0 and curPos==0:
                logAndPrint(logging.info,"Max Number of Cycles Reached:"+str(cycle_num_max))
                flag=false
                time.sleep(60)
            else:
                logAndPrint(logging.info,"Cycle "+str(cycle_count)+" of "+str(cycle_num_max))
                cycle_count=cycle_count+1
                curDest=-1
            

    
logAndPrint(logging.info,"Exiting- Goodbye!")
notify("Starting piLitterRobot","piLitterRobot has used up its "+str(cycle_num_max)+" run cycle(s).")   

playSongOnRepeat(1,finishSong)

#!/usr/bin/python
#from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
#from machine import Pin, PWM
#from utime import sleep
from gpiozero import Buzzer
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone

import datetime
import time
import atexit
import RPi.GPIO as GPIO
import logging

logging.basicConfig(filename='litterbox_main.log', level=logging.DEBUG)#litterbox_main.log log file

prog_version = 1.1
prog_name = "Logging Test Program"
mode = GPIO.getmode()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#console prints messages and logs them to the log file
def logAndPrint(msgMethodType,msg):
    #current_datetime=datetime.datetime.now()#.today().strftime('%Y-%h-%d')
    message=str(current_datetime)+"|"+msg
    print(message)
    msgMethodType(message)
        


# Title Screen
print("---------------------------------")
print("-" + prog_name + " " + str(prog_version) + "  -")
#print("-Date:" + current_datetime.today().strftime('%Y-%h-%d') + "               -")
print("---------------------------------")

time.sleep(2.00)

logAndPrint(logging.debug,"Debug test")
logAndPrint(logging.info,"Info test")
logAndPrint(logging.warning,"Warning test")
logAndPrint(logging.error,"Error test")



print("logging test")





print("Exiting- Goodbye!")



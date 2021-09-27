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

logging.basicConfig(filename='litterbox_main.log', level=logging.DEBUG)

prog_version = 1.0
prog_name = "Logging Test Program"
mode = GPIO.getmode()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def logAndPrint(msgType,msg):
    print(msg)
    message=str(datetime.date.today())+" "+msg
    if msgType=="Debug":
        logging.debug(message)
    elif msgType=="Info":
        logging.info(message)
    elif msgType=="Warning":
        logging.warning(message)
    elif msgType=='Error':
        logging.error(message)
    else:
        logging.error(message)
        


# Title Screen
print("---------------------------------")
print("-" + prog_name + " " + str(prog_version) + "  -")
#print("-Date:" + current_datetime.today().strftime('%Y-%h-%d') + "               -")
print("---------------------------------")

time.sleep(2.00)

logAndPrint("Debug","Debug test")
logAndPrint("Info","Info test")
logAndPrint("Warning","Warning test")
logAndPrint("Error","Error test")



print("logging test")





print("Exiting- Goodbye!")



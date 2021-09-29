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
import os
import configparser
import io

prog_version = 1.0
prog_name = "Configuration Test Program"
mode = GPIO.getmode()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



current_datetime=datetime.date.today()
next_run_datetime=datetime.datetime(2021, 7, 12, 9, 55, 0, 342380)

# Title Screen
print("---------------------------------")
print("-" + prog_name + " " + str(prog_version) + "  -")
#print("-Date:" + current_datetime.today().strftime('%Y-%h-%d') + "               -")
print("---------------------------------")

time.sleep(2.00)

# Load the configuration file
configname= os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Litterbox_main.ini')

config = configparser.ConfigParser()
config.sections()
config.read(configname)


port = config.get("Email", "port")#587  # For starttls
print(port)


print("Exiting- Goodbye!")



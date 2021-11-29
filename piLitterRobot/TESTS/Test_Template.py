#!/usr/bin/python
#from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
#from machine import Pin, PWM
#from utime import sleep
#from gpiozero import Buzzer
#from gpiozero import TonalBuzzer
#from gpiozero.tones import Tone

#import datetime
#import time
#import atexit
#import RPi.GPIO as GPIO
#import os
#import configparser
#import io

#variables
prog_version = 1.0
prog_name = "Template for Test Program"
mode = GPIO.getmode()
current_datetime=datetime.date.today()
next_run_datetime=datetime.datetime(2021, 7, 12, 9, 55, 0, 342380)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#methods and functions here




# Title Screen
print("---------------------------------")
print("-" + prog_name + " " + str(prog_version) + "  -")
#print("-Date:" + current_datetime.today().strftime('%Y-%h-%d') + "               -")
print("---------------------------------")

time.sleep(2.00)

print("Start Test")
#start test code here

print("Exiting Test- Goodbye!")



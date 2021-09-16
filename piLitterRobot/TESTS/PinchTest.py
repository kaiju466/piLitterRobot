#!/usr/bin/python
#from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

import time
import atexit
import RPi.GPIO as GPIO
import ButtonHandler as Button

GPIO_Pinch=24#Pinch Sensor

GPIO.setup(GPIO_Pinch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
cb = Button.ButtonHandler(GPIO_Pinch, real_cb, edge='rising', bouncetime=100)
cb.start()
GPIO.add_event_detect(GPIO_Pinch, GPIO.RISING, callback=cb)

def real_cb():
	print("Test")










#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

import time
import atexit
import RPi.GPIO as GPIO


    

# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

################################# DC motor test!
myMotor = mh.getMotor(2)

intPos=0



# set the speed to start, from 0 (off) to 255 (max speed)
myMotor.setSpeed(250)#150)

while (True):
    
    GPIO.setmode(GPIO.BOARD);
    GPIO.setup(23, GPIO.IN)
    input_value = GPIO.input(23)
    
    print ("inputval:"+str(input_value))
    intPos=intPos+1
    print ("\tRotation:"+str(intPos))
    #myMotor.run(Raspi_MotorHAT.FORWARD);
    #time.sleep(12)#1.6)
    
    
    # turn on motor
    print ("\tStop")
    myMotor.run(Raspi_MotorHAT.RELEASE);
    time.sleep(5.0)
    

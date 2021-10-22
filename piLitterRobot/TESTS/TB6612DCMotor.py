#!/usr/bin/env python

#Code for Adafruit TB6612 motor controller
#https://howchoo.com/g/mjg5ytzmnjh/controlling-dc-motors-using-your-raspberry-pi
#This sample code will drive the motors clockwise for 5 seconds and then counterclockwise for 5 seconds

# Import required modules
import time
import RPi.GPIO as GPIO

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)


#----Pin setup-----------
#STBY = Pin 13 (GPIO #21)

#Motor A:
#PWMA = Pin 7 (GPIO #4)
#AIN2 = Pin 11 (GPIO #17)
#AIN1 = Pin 12 (GPIO #18)

#Motor B:
#BIN1 = Pin 15 (GPIO #22)
#BIN2 = Pin 16 (GPIO #23)
#PWMB = Pin 18 (GPIO #24)



# set up GPIO pins
GPIO.setup(7, GPIO.OUT) #(GPIO #4) Connected to PWMA
GPIO.setup(11, GPIO.OUT) #(GPIO #17)Connected to AIN2
GPIO.setup(12, GPIO.OUT) #(GPIO #18) Connected to AIN1
GPIO.setup(13, GPIO.OUT) #(GPIO #21) Connected to STBY

# Drive the motor clockwise
GPIO.output(12, GPIO.HIGH) # Set AIN1
GPIO.output(11, GPIO.LOW) # Set AIN2

# Set the motor speed
GPIO.output(7, GPIO.HIGH) # Set PWMA

# Disable STBY (standby)
GPIO.output(13, GPIO.HIGH)

# Wait 5 seconds
time.sleep(5)

# Drive the motor counterclockwise
GPIO.output(12, GPIO.LOW) # Set AIN1
GPIO.output(11, GPIO.HIGH) # Set AIN2

# Set the motor speed
GPIO.output(7, GPIO.HIGH) # Set PWMA

# Disable STBY (standby)
GPIO.output(13, GPIO.HIGH)

# Wait 5 seconds
time.sleep(5)

# Reset all the GPIO pins by setting them to LOW
GPIO.output(12, GPIO.LOW) # Set AIN1
GPIO.output(11, GPIO.LOW) # Set AIN2
GPIO.output(7, GPIO.LOW) # Set PWMA
GPIO.output(13, GPIO.LOW) # Set STBY
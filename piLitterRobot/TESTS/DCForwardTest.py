#!/usr/bin/python

from MasterMotorControl import Motor
import time

Dir = [
    'forward',
    'backward',
]




prog_version = 1.0
prog_name = "Waveshare Forward Test Program"

# Title Screen
print("---------------------------------")
print("-" + prog_name + " " + str(prog_version) + "  -")
#print("-Date:" + current_datetime.today().strftime('%Y-%h-%d') + "               -")
print("---------------------------------")

time.sleep(2.00)

print("Start Forward Test")

print("this is a motor driver test code")
Motor = Motor('waveshare')

print("forward")
Motor.MotorRun(0, 'forward', 50)
Motor.MotorRun(1, 'forward', 50)
time.sleep(2)


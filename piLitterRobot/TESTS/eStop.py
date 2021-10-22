#!/usr/bin/python

from waveshare import MotorDriver
import time

prog_version = 1.0
prog_name = "Waveshare Estop Program"

# Title Screen
print("---------------------------------")
print("-" + prog_name + " " + str(prog_version) + "  -")
#print("-Date:" + current_datetime.today().strftime('%Y-%h-%d') + "               -")
print("---------------------------------")

time.sleep(2.00)

print("Start Test")

Motor = MotorDriver()
print("stop")
Motor.MotorStop(0)
Motor.MotorStop(1)
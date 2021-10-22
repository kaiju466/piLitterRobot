#!/usr/bin/python

from waveshare import MotorDriver


prog_version = 1.0
prog_name = "Waveshare Test Program"

# Title Screen
print("---------------------------------")
print("-" + prog_name + " " + str(prog_version) + "  -")
#print("-Date:" + current_datetime.today().strftime('%Y-%h-%d') + "               -")
print("---------------------------------")

time.sleep(2.00)

print("Start Test")

print("this is a motor driver test code")
Motor = MotorDriver()

print("forward 2 s")
Motor.MotorRun(0, 'forward', 100)
Motor.MotorRun(1, 'forward', 100)
time.sleep(2)

print("backward 2 s")
Motor.MotorRun(0, 'backward', 100)
Motor.MotorRun(1, 'backward', 100)
time.sleep(2)

print("stop")
Motor.MotorStop(0)
Motor.MotorStop(1)
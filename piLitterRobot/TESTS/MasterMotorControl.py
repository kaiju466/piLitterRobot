#!/usr/bin/python
#this is an experimental motor driver to attempt to create an interface for the three potential drivers to reduce complexity in design
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from waveshare import MotorDriver

class Motor():
    mdn=""
    
    def __init__(self,motorDrivername):
        global mdn
        mdn=motorDrivername
        if motorDrivername == "waveshare":
            Motor = MotorDriver()
        else:
            Motor=Raspi_motorHAT(addr=0x6f)
        
    
    def MotorRun(self, motor, index, speed):
        global mdn
        if mdn == "waveshare":
            Motor.MotorRun(self,motor, index, speed)
        else:
            if index == "forward":
                Motor.run(Raspi_MotorHAT.FORWARD)
            else:
                Motor.run(Raspi_MotorHAT.Backward)
    
    def MotorStop(self, motor):
        global mdn
        if mdn == "waveshare":
            Motor.MotorStop(motor)
        else:
            Motor.getMotor(motor).run(Raspi_MotorHAT.RELEASE)
            Motor.getMotor(motor).run(Raspi_MotorHAT.RELEASE)
            Motor.getMotor(motor).run(Raspi_MotorHAT.RELEASE)
            Motor.getMotor(motor).run(Raspi_MotorHAT.RELEASE)


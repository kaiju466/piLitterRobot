#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from waveshare import MotorDriver

class Motor():
    mdn=""
    
    def __init__(self,motorDrivername):
        mdn=motorDrivername
        if motorDrivername == "waveshare":
            Motor = MotorDriver()
        else:
            Motor=Raspi_motorHAT(addr=0x6f)
        
    
    def MotorRun(self, motor, index, speed,motorDrivername):
        if motorDrivername == "waveshare":
            Motor.MotorRun(motor, index, speed)
        else:
            if index == "forward":
                Motor.run(Raspi_MotorHAT.FORWARD)
            else:
                Motor.run(Raspi_MotorHAT.Backward)
    
    def MotorStop(self, motor,motorDrivername):
        if motorDrivername == "waveshare":
            Motor.MotorStop(motor)
        else:
            Motor.getMotor(motor).run(Raspi_MotorHAT.RELEASE)
            Motor.getMotor(motor).run(Raspi_MotorHAT.RELEASE)
            Motor.getMotor(motor).run(Raspi_MotorHAT.RELEASE)
            Motor.getMotor(motor).run(Raspi_MotorHAT.RELEASE)


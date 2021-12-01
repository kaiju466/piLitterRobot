import RPi.GPIO as GPIO
from waveshare import MotorDriver
import time
import datetime 

#initialize motor
Motor = MotorDriver()
motorSpeed=50
current_datetime=datetime.datetime.now()

gpios={23:"GPIO_Home",
       24:"GPIO_Dump"}

GPIO.setmode(GPIO.BCM)

GPIO_Dump=23#23#sensor detection for Dump
GPIO_Home=24#sensor detection for Home
#GPIO_PIR=24
counterDump=0
counterHome=0
flag=True

print("KY-003 Module Test With Motor (CTRL-C to exit)")
print("Please make sure to have globe at home position for start of test")

GPIO.setup(GPIO_Dump,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(GPIO_Home,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def printFunction(GPIO_Pin):
    global counterDump,counterHome
    print(" ")
    if GPIO_Pin == GPIO_Dump:#23
        counterDump=counterDump+1
    else:
        counterHome=counterHome+1
        
    print("DateTime:"+str(current_datetime))
    print("Detected "+str(counterDump)+" "+"Dump Pin")
    print("Detected "+str(counterHome)+" "+"Home Pin")
    

GPIO.add_event_detect(GPIO_Dump,GPIO.RISING,callback=printFunction)
GPIO.add_event_detect(GPIO_Home,GPIO.RISING,callback=printFunction)

Motor.MotorStop(0)
Motor.MotorRun(0, 'backward', motorSpeed)

try:
    while flag:
        Current_State = GPIO.input(GPIO_Dump)
        
except KeyboardInterrupt:
    Motor.MotorStop(0)
    print("Goodbye")
        #if GPIO.input(channel):
         #   print("Input was High")
        #else:
        #    print("Input was High")
        #print(Current_State)

        
#GPIO.cleanup



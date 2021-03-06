import RPi.GPIO as GPIO
import time
import datetime 

gpios={23:"GPIO_Home",
       24:"GPIO_Dump"}

GPIO.setmode(GPIO.BCM)

GPIO_Dump=23#23#sensor detection for Dump
GPIO_Home=24#sensor detection for Home
#GPIO_PIR=24
counterDump=0
counterHome=0
flag=True

current_datetime=datetime.datetime.now()

print("KY-003 Module Test (CTRL-C to exit)")

GPIO.setup(GPIO_Dump,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(GPIO_Home,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def printFunction(GPIO_Pin):
    global counterDump,counterHome
    print(" ")
    if GPIO_Pin == 23:
        counterDump=counterDump+1
    else:
        counterHome=counterHome+1
        
    print("DateTime:"+str(current_datetime))
    print("Detected "+str(counterDump)+" "+"Dump Pin")
    print("Detected "+str(counterHome)+" "+"Home Pin")


GPIO.add_event_detect(GPIO_Dump,GPIO.RISING,callback=printFunction)
GPIO.add_event_detect(GPIO_Home,GPIO.RISING,callback=printFunction)




try:
    while flag:
        Current_State = GPIO.input(GPIO_Dump)
except KeyboardInterrupt:
    print("Goodbye")
        #if GPIO.input(channel):
         #   print("Input was High")
        #else:
        #    print("Input was High")
        #print(Current_State)

        
#GPIO.cleanup



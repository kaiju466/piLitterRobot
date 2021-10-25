import RPi.GPIO as GPIO

gpios={22:"GPIO_Home",
       27:"GPIO_Dump"}

GPIO.setmode(GPIO.BCM)

GPIO_Dump=27#23#sensor detection for Dump
GPIO_Home=22#sensor detection for Home
#GPIO_PIR=24
counterDump=0
counterHome=0
flag=True

print("KY-003 Module Test (CTRL-C to exit)")

GPIO.setup(GPIO_Dump,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(GPIO_Home,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def printFunction(GPIO_Pin):
    global counterDump,counterHome
    
    if GPIO_Pin == 27:
        counterDump=counterDump+1
        print("Detected "+str(counterDump)+" "+gpios[GPIO_Pin])
    else:
        counterHome=counterHome+1
        print("Detected "+str(counterHome)+" "+gpios[GPIO_Pin])


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



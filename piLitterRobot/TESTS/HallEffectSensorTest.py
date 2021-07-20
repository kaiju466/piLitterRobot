import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO_PIR=24
counter=1
flag=True

print("KY-003 Module Test (CTRL-C to exit)")

GPIO.setup(GPIO_PIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)
def printFunction(GPIO_PIR):
    global counter
    print("Detected "+str(counter))
    counter=counter+1

GPIO.add_event_detect(GPIO_PIR,GPIO.RISING,callback=printFunction)



try:
    while flag:
        Current_State = GPIO.input(GPIO_PIR)
except KeyboardInterrupt:
    print("Goodbye")
        #if GPIO.input(channel):
         #   print("Input was High")
        #else:
        #    print("Input was High")
        #print(Current_State)

        
#GPIO.cleanup


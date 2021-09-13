#!/usr/bin/python
#from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
#from machine import Pin, PWM
#from utime import sleep
from gpiozero import Buzzer
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone

import time
import atexit
import RPi.GPIO as GPIO


prog_version = 1.0
prog_name = "Buzzer Test Program"
mode = GPIO.getmode()

# GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#GPIO_PIR = 27  # 23#sensor detection for Home
#GPIO_PIR2 = 22  # sensor detection for Dump
GPIO_Buzzer = 27  # buzzer pin
#GPIO.setup(27, GPIO.OUT)
#GPIO_Buzzer = GPIO.PWM(17, 100)
#GPIO_Buzzer.start(5)
#time.sleep(2)

# GPIO_OverRide=#button used for manual run
# GPIO_STATLIGHT=#led used to indicate finished status and issues# Blick=issue,On=Done,Off=Ok

# counter=1
# counter2=1

#https://www.tomshardware.com/how-to/buzzer-music-raspberry-pi-pico

#buzzer = PWM(Pin(GPIO_Buzzer))


# GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# cb = ButtonHandler(4, real_cb, edge='rising', bouncetime=100)
# cb.start()
# GPIO.add_event_detect(4, GPIO.RISING, callback=cb)

# datetime.datetime(2020, 5, 17)

# create a default object, no changes to I2C address or frequency
#mh = Raspi_MotorHAT(addr=0x6f)  # default address: 0x6f

# initialize motor

    # elif

    # mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)

#buzzer=Buzzer(GPIO_Buzzer)
b = TonalBuzzer(GPIO_Buzzer)


def buzz():
    print("buzz")
    buzzer.on()
    time.sleep(0.1)
    buzzer.off()
    time.sleep(0.2)
    #playtone(262)


#def bequiet():
    #buzzer.duty_u16(0)

#Note range A3-G5
def playtone(frequency):
    b.play(Tone(frequency))
    time.sleep(0.5)
    b.stop()

def finishSong():
    song = ["A4","P","B4","C4"]
    song=song[::-1]
    playsong(song)

def troubleSong():
    song = ["A3","A4","A5"]
    song=song[::-1]
    playsong(song)

def startupSong():
    song = ["A4","P","B4","C4"]
    playsong(song)

def ode2JoySong():
    song = ["C4","C4","D4","E4","P","E4","D4","C4","B3","P","B3","B3","C4","D4"]
    playsong(song)

    
def playsong(mysong):
    #print(str(len(mysong)))
    for i in range(len(mysong)):
        if (mysong[i] == "P"):
            time.sleep(0.25)
        else:
            playtone(mysong[i])
        
    

#def playsong(mysong):
#    for i in range(len(mysong)):
#        if (mysong[i] == "P"):
#            bequiet()
#        else:
#            playtone(tones[mysong[i]])
 #       sleep(0.3)
#    bequiet()


# Title Screen
print("---------------------------------")
print("-" + prog_name + " " + str(prog_version) + "  -")
#print("-Date:" + current_datetime.today().strftime('%Y-%h-%d') + "               -")
print("---------------------------------")

time.sleep(2.00)

# main
#while (flag):

#buzz()
#Ode2JoySong()
print("PlAYING SONG")
#startupSong()
#time.sleep(2.00)
#ode2JoySong()
#finishSong()
#time.sleep(4.00)
troubleSong()
#bequiet()

print("Exiting- Goodbye!")



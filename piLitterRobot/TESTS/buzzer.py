#!/usr/bin/python
#from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
#from machine import Pin, PWM
#from utime import sleep
from gpiozero import Buzzer
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone

import datetime
import time
import atexit
import RPi.GPIO as GPIO


prog_version = 1.0
prog_name = "Buzzer Test Program"
mode = GPIO.getmode()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_Buzzer = 26  # buzzer pin

b = TonalBuzzer(GPIO_Buzzer)

current_datetime=datetime.date.today()
next_run_datetime=datetime.datetime(2021, 7, 12, 9, 55, 0, 342380)
next_song_run=datetime.datetime(2021, 7, 12, 9, 55, 0, 342380)

def buzz():
    print("buzz")
    buzzer.on()
    time.sleep(0.1)
    buzzer.off()
    time.sleep(0.2)


#Note range A3-G5
def playtone(frequency):
    b.play(Tone(frequency))
    time.sleep(0.5)
    b.stop()

def finishSong():
    song = ["A4","P","B4","C4"]
    song=song[::-1]
    playsong(song)
    #return 0

def troubleSong():
    song = ["A3","A4","A5"]
    song=song[::-1]
    playsong(song)

def startupSong():
    song = ["A4","P","B4","C4"]
    playsong(song)

def ode2JoySong():
    song = ["C4","C4","D4","E4","E4","D4","C4","B3","B3","B3","C4","D4","D4","C4","C4"]
    playsong(song)
def songOfStorms():
    song = ["D4","E4","D4",
            "D4","E4","D4",
            "E4","F4","E4",
            "F4","E4","C4",
            "A4","A4","D4","F4","G4"]
    playsong(song)
def bolaroOfFire():
    song = ["C4","C4","D4","E4","E4","D4","C4","B3","B3","B3","C4","D4","D4","C4","C4"]
    playsong(song)
def songOfTime():
    song = ["A4","D4","F4","P",
            "A4","D4","F4","P",
            
            "A4","C4","B4",
            
            "G4","F4","G4",
            "A4","D4","C4",
            "E4","D4"]
    playsong(song)
    
def playsong(mysong):
    #print(str(len(mysong)))
    for i in range(len(mysong)):
        if (mysong[i] == "P"):
            time.sleep(0.10)
        else:
            playtone(mysong[i])
        
#play finish song every # min 
def playFinishSongRepeat(time):
    global current_datetime,next_song_run
    while (True):
        #next_song_run
        current_datetime=datetime.datetime.now()
        if current_datetime>=next_song_run:
            print("Playing finishSong every "+str(time)+" minutes")
            finishSong()
            next_song_run=(datetime.datetime.now() + datetime.timedelta(minutes=time))#minutes=numInterval_Hours))#
            print("Playing next song at "+str(next_song_run))
            
#play song every # min 
def playSongOnRepeat(time,methodToRun):
    global current_datetime,next_song_run
    while (True):
        #next_song_run
        current_datetime=datetime.datetime.now()
        if current_datetime>=next_song_run:
            print("Playing Song every "+str(time)+" minute(s)")
            methodToRun()
            next_song_run=(datetime.datetime.now() + datetime.timedelta(minutes=time))#minutes=numInterval_Hours))#
            print("Playing next song at "+str(next_song_run))


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
#songOfTime()
playSongOnRepeat(1,finishSong)
#finishSong()
#time.sleep(4.00)
#troubleSong()
#bequiet()
#playFinishSongRepeat(1)

print("Exiting- Goodbye!")



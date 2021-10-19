# piLitterRobot
Code for basic integration of Raspberry Pi into Litter-Robot 3 using a GeekWorm Pi MotorHat or Adafruit TB6612 motor controller

Parts list:
  Raspberry Pi 3b(any pi with a gpio should potentially work though weak hardware will be slow)
  LitterRobot3
  12V powersupply (or original Litter-Robot 3 powersupply)
  5V powersupply or voltage transformer(can use a dedicated supply or modify a carlighter usb adaptor)
  3144E A3144 KY-003 HallEffect Sensors(2)
  GeekWorm PiMotorHat or Adafruit TB6612 motor controller
 
 
Implementation:
  Suggested implementation is to install supervisorctl and setup the scripts(litterbox_main.py and litterbox_flask) to run on piboot. If successful, the flask website will show up in a webbrower at http://{rpi's ipaddress}:5000. it should be noted that Litterbox will automatically begin a calibration cycle when started in order to hone known position in software.
  
Note: Current Hardware itteration is a prototype and majority of parts are in a separate plastic case due to limited space in the existing hardware.

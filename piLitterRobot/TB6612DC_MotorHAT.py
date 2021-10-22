#!/usr/bin/python

#from Raspi_PWM_Servo_Driver import PWM
import time

#----Pin setup-----------
#STBY = Pin 13 (GPIO #21)

#Motor A:
#PWMA = Pin 7 (GPIO #4)
#AIN2 = Pin 11 (GPIO #17)
#AIN1 = Pin 12 (GPIO #18)

#Motor B:
#BIN1 = Pin 15 (GPIO #22)
#BIN2 = Pin 16 (GPIO #23)
#PWMB = Pin 18 (GPIO #24)
		
class TB6612_DCMotor:#Raspi_DCMotor:
	def __init__(self, controller, num):
		self.MC = controller
		self.motornum = num
		self.STBYpin = 13 #STBY
		#pwm = in1 = in2 = 0

		if (num == 0):
			pwm = 7
			in2 = 11
			in1 = 12
		elif (num == 1):
			pwm = 15
			in2 = 16
			in1 = 18
		else:
			raise NameError('TB6612DC Motor must be between 0 and 1 inclusive')
		self.PWMpin = pwm
		self.IN1pin = in1
		self.IN2pin = in2

	def run(self, command):
		if not self.MC:
			return
		if (command == TB6612_MotorHAT.FORWARD):
			self.MC.setPin(self.IN2pin, 0)
			self.MC.setPin(self.IN1pin, 1)
		if (command == TB6612_MotorHAT.BACKWARD):
			self.MC.setPin(self.IN1pin, 0)
			self.MC.setPin(self.IN2pin, 1)
		if (command == TB6612_MotorHAT.RELEASE):
			self.MC.setPin(self.IN1pin, 0)
			self.MC.setPin(self.IN2pin, 0)
	def setSpeed(self, speed):
		if (speed < 0):
			speed = 0
		if (speed > 255):
			speed = 255
		self.MC._pwm.setPWM(self.PWMpin, 0, speed*16)

class TB6612DC_MotorHAT:
	FORWARD = 1
	BACKWARD = 2
	BRAKE = 3
	RELEASE = 4

	SINGLE = 1
	DOUBLE = 2
	INTERLEAVE = 3
	MICROSTEP = 4

	def __init__(self, freq = 1600)#, addr = 0x60, freq = 1600):
		
		self.motors = [ TB6612_DCMotor(self, m) for m in range(2) ]
        #self._pwm =  PWM(addr, debug=False)
		#self._pwm.setPWMFreq(self._frequency)

	def setPin(self, pin, value):
		if (pin < 0) or (pin > 15):
			raise NameError('PWM pin must be between 0 and 15 inclusive')
		if (value != 0) and (value != 1):
			raise NameError('Pin value must be 0 or 1!')
		if (value == 0):
			self._pwm.setPWM(pin, 0, 4096)
		if (value == 1):
			self._pwm.setPWM(pin, 4096, 0)
	#def GetPin(self, pin):
	#	if (pin < 0) or (pin > 15):
	#		raise NameError('PWM pin must be between 0 and 15 inclusive')
	#	if (value == 0):
	#		self._pwm.setPWM(pin, 0, 4096)
	#	if (value == 1):
	#		self._pwm.setPWM(pin, 4096, 0)

	def getMotor(self, num):
		if (num < 1) or (num > 2):
			raise NameError('MotorHAT Motor must be between 1 and 2 inclusive')
		return self.motors[num-1]

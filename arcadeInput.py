#!/usr/bin/env python
# arcadeInput.py
#
# Kevin Hughes and Jonathan Johnstone Hack Labs Kingston Team "25c to Play"
#
# Feb 2013
# 

"""
GPIO to Joystick/Keyboard for Raspberry Pi
based on rpi-gpio-jstk.py by Chris Swan http://blog.thestateofme.com/2012/08/10/raspberry-pi-gpio-joystick/
based on Example Usage https://code.google.com/p/raspberry-gpio-python/
based on python-uinput/examples/joystick.py by tuomasjjrasanen
https://github.com/tuomasjjrasanen/python-uinput/blob/master/examples/joystick.py
requires uinput kernel module (sudo modprobe uinput)
requires python-uinput (git clone https://github.com/tuomasjjrasanen/python-uinput) or sudo apt-get install python-uinput
requires (from http://pypi.python.org/pypi/RPi.GPIO/0.3.1a)
"""

import time
import signal
import sys
import RPi.GPIO as GPIO
import uinput

# uinput device
events = (uinput.KEY_W, uinput.KEY_A, uinput.KEY_S, uinput.KEY_D)
#events = (uinput.BTN_JOYSTICK, uinput.ABS_X + (0, 255, 0, 0), uinput.ABS_Y + (0, 255, 0, 0))
device = uinput.Device(events)

class button(object):
	def __init__ (self, button, key):
		self.button = button
		self.key = key
		self.was_pressed = False
	def poll(self):
		if ( GPIO.input(self.button) == 1 and not self.was_pressed) :
			device.emit(self.key, 1) # Press.
			self.was_pressed = True
		elif  ( GPIO.input(self.button) == 0 and self.was_pressed) :
			device.emit(self.key, 0) # Release.
			self.was_pressed = False
		
def main():
	signal.signal(signal.SIGINT, signal_handler)
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	pinBtn = 25
	GPIO.setup(pinBtn,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	pinLED = 18
	GPIO.setup(pinLED,GPIO.OUT)
	LEDon = False
	GPIO.output(pinLED, LEDon)
	# button mappings
	#button1 = 11
	#GPIO.setup(button1, GPIO.IN)

	# Polling
	was_pressed = False
	GPIO.output(pinLED, 1)
	time.sleep(1)
	GPIO.output(pinLED, LEDon)
	b = button(pinBtn, uinput.KEY_A)
	while True:
		b.poll()
		time.sleep(0.1)

def signal_handler(signal, frame):
	print "exiting"
	GPIO.cleanup()
	sys.exit(0)

if __name__ == "__main__":
	main()

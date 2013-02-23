#!/usr/bin/env python
# arcadeInput.py
#
# Kevin Hughes, Jonathan Johnstone, and Ryan d'Eon -  Hack Labs Kingston Team "25c to Play"
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
events = (uinput.KEY_UP, uinput.KEY_LEFTCTRL, uinput.KEY_SPACE, uinput.KEY_ESC)
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

	#Arrows
	pinUP = 2
	pinDOWN = 3
	pinLEFT = 4
	pinRIGHT = 7

	GPIO.setup(pinUP   , pull_up_down=GPIO.PUD_UP)
	GPIO.setup(pinDOWN , pull_up_down=GPIO.PUD_UP)
	GPIO.setup(pinLEFT , pull_up_down=GPIO.PUD_UP)
	GPIO.setup(pinRIGHT, pull_up_down=GPIO.PUD_UP)

	#Keys

	pinA = 27
	pinB = 22
	pinCOIN = 10
	pinSTART = 9

	GPIO.setup(pinA    ,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(pinB    ,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(pinCOIN ,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(pinSTART,GPIO.IN, pull_up_down=GPIO.PUD_UP)

	# Polling
	#Arrows
	button_UP = button(pinUP, uinput.KEY_UP)
	button_DOWN = button(pinUP, uinput.KEY_DOWN)
	button_LEFT = button(pinUP, uinput.KEY_LEFT)
	button_RIGHT = button(pinUP, uinput.KEY_RIGHT)
	#keys
	button_A = button(pinUP, uinput.KEY_SPACE)
	button_B = button(pinUP, uinput.KEY_LEFTCTRL)
	#button_COIN = button(pinUP, uinput.KEY_UP)
	#button_START = button(pinUP, uinput.KEY_UP)
	
	buttons = [button_UP, button_DOWN,button_LEFT, button_RIGHT,button_A,button_B]
	while True:
		for input_button in buttons:
			input_button.poll()
		time.sleep(0.02)

def signal_handler(signal, frame):
	print "exiting"
	GPIO.cleanup()
	sys.exit(0)

if __name__ == "__main__":
	main()

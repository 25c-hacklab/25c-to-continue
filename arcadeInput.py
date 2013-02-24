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
import subprocess

# uinput device
events = (uinput.KEY_UP, uinput.KEY_DOWN, uinput.KEY_LEFT, uinput.KEY_RIGHT, uinput.KEY_Z, uinput.KEY_SPACE, uinput.KEY_ESC)
#events = (uinput.BTN_JOYSTICK, uinput.ABS_X + (0, 255, 0, 0), uinput.ABS_Y + (0, 255, 0, 0))
device = uinput.Device(events)

class button(object):
	def __init__ (self, button, key):
		self.button = button
		self.key = key
		self.was_pressed = False
	def poll(self):
		if ( GPIO.input(self.button) == 0 and not self.was_pressed) :
			device.emit(self.key, 1) # Press.
			self.was_pressed = True
		elif  ( GPIO.input(self.button) == 1 and self.was_pressed) :
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
	pinRIGHT = 17

	GPIO.setup(pinUP   ,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(pinDOWN ,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(pinLEFT ,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(pinRIGHT,GPIO.IN, pull_up_down=GPIO.PUD_UP)

	#Keys

	pinA = 27
	pinB = 22
	pinCOIN = 9
	pinSTART = 10

	GPIO.setup(pinA    ,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(pinB    ,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(pinCOIN ,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(pinSTART,GPIO.IN, pull_up_down=GPIO.PUD_UP)

	# Polling
	#Arrows
	button_UP = button(pinUP, uinput.KEY_UP)
	button_DOWN = button(pinDOWN, uinput.KEY_DOWN)
	button_LEFT = button(pinLEFT, uinput.KEY_LEFT)
	button_RIGHT = button(pinRIGHT, uinput.KEY_RIGHT)
	#keys
	button_A = button(pinA, uinput.KEY_SPACE)
	button_B = button(pinB, uinput.KEY_Z)
	button_COIN = button(pinCOIN, uinput.KEY_ESC)
	
	
	buttons = [ button_DOWN,button_LEFT, button_RIGHT, button_UP, button_A,button_B,button_COIN]
	
	button_start_pressed = False
	while True:
		for input_button in buttons:
			input_button.poll()
		## Start button
		if ( GPIO.input(pinSTART) == 0 and not button_start_pressed) :
			start_script ()
			button_start_pressed = True
		elif  ( GPIO.input(pinSTART) == 1 and button_start_pressed) :
			button_start_pressed = False
		time.sleep(0.02)

def signal_handler(signal, frame):
	print "exiting"
	GPIO.cleanup()
	sys.exit(0)
def start_script ():
	subprocess.Popen("/home/pi/25c-to-continue/startup_script.bash")
if __name__ == "__main__":
	main()

# arcadeInput.py
#
# Kevin Hughes and Hack Labs Kingston Team "25c to Play"
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

def main():
	signal.signal(signal.SIGINT, signal_handler)
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	# button mappings
	button1 = 11
	GPIO.setup(button1, GPIO.IN)

	# uinput device
	events = (uinput.KEY_W, uinput.KEY_A, uinput.KEY_S, uinput.KEY_D)
	#events = (uinput.BTN_JOYSTICK, uinput.ABS_X + (0, 255, 0, 0), uinput.ABS_Y + (0, 255, 0, 0))
	device = uinput.Device(events)

	# Polling
	#while(True):
		#pass
	
	# Interrupt Drive

def signal_handler(signal, frame):
	print "exiting"
	GPIO.cleanup()
	sys.exit(0)

if __name__ == "__main_":
	main()

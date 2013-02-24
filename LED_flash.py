#!/usr/bin/env python

import RPi.GPIO as GPIO, time
import signal
import sys	

def main():
	signal.signal(signal.SIGINT, signal_handler)

	GPIO.setmode(GPIO.BCM)	
	GPIO.setwarnings(False)
	GREEN_LED = 18
	RED_LED = 23
	GPIO.setup(GREEN_LED, GPIO.OUT)
	GPIO.setup(RED_LED, GPIO.OUT)

	Green_bool = True
	Red_bool = False

	while True:
    		GPIO.output(GREEN_LED, Green_bool)
    		GPIO.output(RED_LED, Red_bool)

    		Green_bool = not Green_bool
    		Red_bool = not Red_bool

    		time.sleep(1)

def signal_handler(signal,frame):
	GPIO.cleanup()
	sys.exit(0)

if __name__ == "__main__":
	main()

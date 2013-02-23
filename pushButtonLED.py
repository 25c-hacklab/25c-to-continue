import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pinBtn = 25
GPIO.setup(pinBtn,GPIO.IN, pull_up_down=GPIO.PUD_UP)
pinLED = 18
GPIO.setup(pinLED,GPIO.OUT)
LEDon = False
GPIO.output(pinLED, LEDon)

# Polling
while(True):
	GPIO.output(pinLED,0)
	while(GPIO.input(pinBtn)==0):
		GPIO.output(pinLED,1)


# Interrupt Driven
"""
GPIO.set_high_event(pinBtn)
while(True):
	if(GPIO.event_detected(pinBtn)):
		print 'button pushed!'
		LEDon = not LEDon
		GPIO.output(pinLED,LEDon)
"""

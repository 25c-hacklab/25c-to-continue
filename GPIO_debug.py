
import time
#import signal
import sys
import RPi.GPIO as GPIO
#import uinput


GPIO_list = [-1, -1, -1, 2, -1, 3, -1, 4, 14, -1, 15, 17, 18, 27, -1, 22, 23, -1, 24, 10, -1, 9, 25, 11, 8, -1, 7]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for port in GPIO_list:
    if (port != -1):
        print port
        GPIO.setup(port,GPIO.IN, pull_up_down=GPIO.PUD_UP)

while (True):
    for port in GPIO_list:
        if (port != -1):
            sys.stdout.write(str(port))
            sys.stdout.write("\t")
    print ''
    for port in GPIO_list:
        if (port != -1):
            sys.stdout.write(str(int(GPIO.input(port))))
            sys.stdout.write("\t")
    print ''
    time.sleep(1)
    

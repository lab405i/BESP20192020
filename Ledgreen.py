#!/usr/bin/python

Author: Tanya Litvinenko

#Flashing green LED with a button and a delay of 0.5 seconds.

import RPi.GPIO as GPIO
from time import sleep
GREEN_PIN = 29
BUTTON_PIN = 40
print ("RPi.GPIO init start")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
print ("RPi.GPIO init end")
print ("GPIO setup")
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(GREEN_PIN, 1)

while True:
inp = GPIO.input(BUTTON_PIN)
if inp==0:
GPIO.output(GREEN_PIN, 1)
sleep(0.5)
GPIO.output(GREEN_PIN, 0)
sleep(0.5)        

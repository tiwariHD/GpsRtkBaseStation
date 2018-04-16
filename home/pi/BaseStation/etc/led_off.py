#!/usr/bin/python
################################################################################
# File:         led_off.py
# Usage:        Cleanup script 
# Description:  Switches off all LEDs and stops all running processes
################################################################################

import RPi.GPIO as GPIO
from subprocess import call

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.output(4, False)

GPIO.setup(18, GPIO.OUT)
GPIO.output(18, False)

GPIO.setup(23, GPIO.OUT)
GPIO.output(23, False)

#Sending SIGUSR2 to rtkrcv
call(['sudo', 'pkill', '-12', 'rtkrcv'])

#sending SIGINT to str2str
call(['sudo', 'pkill', '-2', 'str2str'])

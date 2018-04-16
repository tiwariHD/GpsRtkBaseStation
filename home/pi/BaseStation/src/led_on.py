#!/usr/bin/python
################################################################################
# File:         led_on.py
# Usage:        Called from rc.local to denote Raspberry Pi switched ON 
# Description:  Switches on LED at pin position 7 and ground
################################################################################

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, True)

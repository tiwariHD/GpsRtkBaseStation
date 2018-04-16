#!/bin/bash
################################################################################
# File:         test.sh
# Usage:        Test script to start BaseStation in Monitor mode.
# Description:  This script can be used to start BaseStation manually
#		for debugging purposes.
################################################################################

BST='/home/pi/BaseStation'
python $BST/src/led_on.py &
/bin/bash $BST/src/ppp.sh &
python $BST/src/base.py > $BST/logs/py_log.txt &


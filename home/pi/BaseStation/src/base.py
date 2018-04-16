#!/usr/bin/python
################################################################################
# File:         base.py
# Usage:        Invocation after boot from /etc/rc.local
# Description:  Program reads from nmea data file, which is updated
#               in realtime by the rtkrcv server
################################################################################

###
# Headers
###
import time
import timeit
import sys
import RPi.GPIO as GPIO
from subprocess import call

###
# Function:     led_ppp
# Description:  Switches on Red LED for ppp mode
###
def led_ppp():
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(18, True)

###
# Function:     led_base
# Description:  Switches off Red LED and on Yellow for Basestation mode 
###
def led_base():
	GPIO.setup(18, GPIO.OUT)
	GPIO.output(18, False)
	GPIO.setup(23, GPIO.OUT)
	GPIO.output(23, True)

###
# Function:     tail_f
# Description:  reads data from file one line at a time
###
def tail_f(file):
        
	while True:
		where = file.tell()
		line = file.readline()

		if not line:
			time.sleep(1)
			file.seek(where)

		else:
			yield line

###
# Function:     main
# Decription:   Checks whether gps data received is good,
#               then calls script for RTCM transmission to rover
###

def main():

        time.sleep(2)
	GPIO.setmode(GPIO.BCM)
	#Red LED on for ppp mode
 	led_ppp()
 	
        gsa = False
        gsv = False
        #File where rtkrcv saves nmea data
        filename = '/home/pi/BaseStation/solution/ht_sol.pos'
        
        print 'python program start, will sleep for 30 sec then check gps data'
        start = timeit.default_timer()
        time.sleep(30)

        try:
                #Returns one line at a time of nmea data
                for line in tail_f(open(filename)):
                        
                        temp = line.split(',')
                        #checking for 3D fix and PDOP < 4
                        #ex: $GPGSA,A,3,02,12,14,25,26,29,31,,,,,,2.0,1.4,1.4,1*23
                        if (temp[0] == '$GPGSA') and (temp[2] == '3') and (float(temp[15]) < 4.0):
                                print '3D fix received, PDOP:', temp[15] 
                                gsa = True

                        #checking for no of satellites >= 7, in line no. 1(GPGSV has mulitple lines)
                        #ex: $GPGSV,2,1,07,02,27,049,41,12,21,102,46,14,16,248,38,25,64,097,47,1*61
                        if (temp[0] == '$GPGSV') and (temp[2]== '1') and (int(temp[3]) >= 7):
                                print temp[3], 'satellites in view'		
                                gsv = True

                        #if both conditions satisfied then stop ppp mode
                        if gsa and gsv:
                                print 'good data acheived'
                                break
                        

        except KeyboardInterrupt:
                print 'SIGKILL received, closing now'
                quit()

        stop = timeit.default_timer()

        #Sending SIGUSR2 to rtkrcv which stops the rtkrcv server
        print 'closing rtkrcv, total time(includes 30 sec sleep):', stop - start
        call(['sudo', 'pkill', '-12', 'rtkrcv'])

        time.sleep(2)
        #Calling the basestation script now
        print 'now starting RTCM transmission using str2str'
        #Red LED off and Yellow LED on for basestation
	led_base()
        call(['/bin/bash', '/home/pi/BaseStation/src/base.sh', '&'])

if __name__ == "__main__":
        main()


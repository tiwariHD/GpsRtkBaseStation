#!/bin/bash
################################################################################
# File:         base.sh
# Usage:        Invocation from base.py after good gps data is received
# Description:  Calls str2str to start basestation mode,
#		which transmits RTCM data to rover through XBee devices.
################################################################################

#Station coordinates(known beforehand, can also be passed as arguments)
LAT=49.4166918694
LON=8.6750963222
ALT=158.54

#Station ID of the Xbee devices
SID=2222

#Message IDs of RTCM messages to be transmitted
RMSG="1004,1019,1012,1020,1006,1008"

sudo str2str -in serial:///ttyUSB0:115200:8:n:1#ubx -out serial:///ttyUSB1:115200:8:n:1#rtcm3 -c /home/pi/BaseStation/configs/rtk.conf -p $LAT $LON $ALT -sta $SID -msg $RMSG &

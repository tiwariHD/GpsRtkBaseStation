# GpsRtkBaseStation
Enables a Raspberry Pi 3 model to be used as a GPS BaseStation for a GPS enabled rover.

System Components include:

    Raspberry Pi (Version 3 Model B)
    GPS Receiver (U-Blox Neo M8T)
    Two LEDs
    GPS antenna
    2 x Radio Transceiver (Xbee-radio S6B)

This repository uses two programs, rtkrcv and str2str, from RTKLIB 2.4.2.

Code structure:

    -- /home/pi/BaseStation/
	  -- configs  :	Contains config files used by BaseStation 
	  -- etc      :	Extra scripts to run BaseStation when connected with a monitor.
	  -- logs     :	Output directory for logs
	  -- solution :	Stores the NMEA data log file containing location data
	  -- src      :	Source code for BaseStaion
	
    -- /etc/
	  -- rc.local :	Starts BaseStation in Standalone mode, run after bootup

BaseStation code execution begins after bootup from /etc/rc.local script.

For testing in monitor mode afer bootup, use /home/pi/BaseStation/etc/test.sh script.

To switch off LED run /home/pi/BaseStation/etc/led_off.py

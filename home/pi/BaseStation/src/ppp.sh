#!/bin/bash
################################################################################
# File:         ppp.sh
# Usage:        Invocation after boot from /etc/rc.local
# Description:  Performs initial setup, then calls rtkrcv to start ppp mode
################################################################################

sleep 1

sudo rm -f /home/pi/BaseStation/solution/ht_sol.pos

touch /home/pi/BaseStation/solution/ht_sol.pos

sleep 1

sudo rtkrcv -s -o /home/pi/BaseStation/configs/rtk.conf -d /dev/tty1 > /dev/null &

#!/bin/bash

#########################################################
: '
c_date=$(date)
echo "$c_date" >> time.log
'

#########################################################
: '
c_date=$(date)
echo "Date: $c_date"
c_user=$(whoami)
echo "User: $c_user"
d_usage=$(df / | awk 'NR==2 {print $5}')
echo "Disk Usage: $d_usage"
'
#########################################################

c_date=$(date)
echo "Date: $c_date"
c_user=$(whoami)
echo "User: $c_user"
d_usage=$( df / | awk 'NR==2 {print $5}' | tr -d '%' )
if [ "$d_usage" -gt 80 ]; then
    echo "WARNING: Disk Usage High"
else
    echo "Disk is Normal"
fi
#!/bin/bash
if [ "$1" == "" ] # If the input variable does not contain anything, then print "You forgot an IP address!
then
echo "You forgot an IP address!"
echo "Syntax: ./ipsweep.sh <ip range>"
# If nothing is in user input then you forgot an IP address

else
for ip in `seq 1 254` ; do
ping -c 1 $1.$ip | grep '64 bytes' | cut -d " " -f 4 | tr -d ":" &								   # not have to perform the process one IP at a time
done
fi

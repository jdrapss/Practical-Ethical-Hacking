#!/bin/python3

# Goal is to be able to run python3 scanner.py <ip> and scan a designated port range and return the results
# This tool is slower because it scans one port at a time and timesout after 1 second
import sys
import socket
from datetime import datetime as dt

# Define our target
if len(sys.argv) == 2: #argv -> think $variable$ in bash
	target = socket.gethostbyname(sys.argv[1]) # Translating a hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")
	
# Add a pretty banner
print("-" * 50)
print("Scanning target " +target)
print("Time started: "+str(dt.now()))
print("-" * 50)

try: # Used if we need exceptions
	for port in range(1,65535): 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) # Returns an error indicator
		#print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt: # If there is a keyboard interrupt like Ctrl + C then exit
	print("\nExiting program.")
	sys.exit()

except socket.gaierror: # If no host resolution, exit the program
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error: # If we cannot connect to IP we specified, then exit the program
	print("Couldn't connect to server.")
	sys.exit()
	

	
	
		
		
		

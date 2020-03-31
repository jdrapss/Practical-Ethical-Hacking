#!/bin/python3

import socket

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET - Think about IPv4. We are connecting over an IPv4 connection
# SOCK_STREAM - Think of this as a port

s.connect((HOST,PORT))

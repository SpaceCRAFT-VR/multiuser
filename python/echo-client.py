#!/usr/bin/env python3
#from https://realpython.com/python-sockets/

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

#Creation of socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    #Connection to server
    s.connect((HOST, PORT))

    #Send Hello World Message
    s.sendall(b'Hello, world')

    #Read the server's reply and print it
    data = s.recv(1024)

print('Received', repr(data))
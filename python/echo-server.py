#!/usr/bin/env python3
#From Tutorial at https://realpython.com/python-sockets/

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

#Create a socket object (AF_INET = IPv4, SOCK_STREAM = TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    #Bind associates socket with specific network interface and port number
    s.bind((HOST, PORT))

    #listen() enables server to accept() connections, making a listening socket
    s.listen()

    #accept() gives us a new socket object to communicate with the client
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
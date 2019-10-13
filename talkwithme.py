# # # # # # # # # #
#coding:UTF-8
# # # # # # # # # 

# # # # # # # #
#!/usr/bin/env python2.7
# # # # # # #

# # # # # #
# Created November 25th 2017
# Copyright (c) 2017 Beyar.
# # # #

# # #
# Name: talkwithme.py
# #

# Library
import os
import socket
import time

# Clear
os.system("clear")

# Variables
create = 0
available = 0
setup = 0
tick = 0
refreshPort = 0

print "Create connection: 1"
print "Open connection: 2"
creOpen = raw_input("> ")

if creOpen == "1":
	create = 1
	setup = 1
elif creOpen == "2":
	available = 1
	setup = 1

while create == 1:
	available = 0
	if setup == 1:
		# Host adress
	        os.system("ifconfig | grep inet")
		hostNumber = raw_input("Host: ")
		# Port number
		portNumber = input("Port: ")
		# Remote host
		reconnectHost = raw_input("Incoming-Host: ")
		#reconnectHost = hostNumber
		# Remote port number
		reconnectPort = input("Incoming-Port: ")
		primaryserverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		primaryserverSocket.bind((hostNumber, portNumber))
		primaryserverSocket.listen(100)
		os.system("clear")
	print "Your details"
	print "Host: %s" %(hostNumber)
	print "Port: %s" %(portNumber)
	print "Incoming details"
	print "Host: %s" %(reconnectHost)
	print "Port: %s" %(reconnectPort)
	print
	print "Waiting for incoming connections..."
	while True:
		tick += 1
		if tick == 3:
			refreshPort == 1
		clientSocket, addr = primaryserverSocket.accept()
		currentTime = time.ctime(time.time()) + "\r\n"
		clientSocket.send(currentTime.encode("utf-8"))
		receiveMessage = raw_input("You: ")
		renderMsg = "%s | (H: %s R: %s F: %d)" %(receiveMessage, portNumber, reconnectPort, refreshPort) # H = HostPort # R = RemotePort # F = RefreshPort
		clientSocket.send(renderMsg.encode("utf-8"))
		clientSocket.close()
		deliversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		deliversocket.connect((reconnectHost, reconnectPort))
		message = deliversocket.recv(64)
		print
		print "Response from %s" % str(addr)
		print "Connected: %s" %(message.decode("utf-8"))
		deliversocket.close()

while available == 1:
	create = 0
	if setup == 1:
		# Host adress
		connectHost = raw_input("Server-Host: ")
		# Port number
		connectPort = input("Server-Port: ")
		os.system("ifconfig | grep inet")
		# Remote host
		remoteHost = raw_input("Client-Host: ")
		#remoteHost = connectHost
		# Remote port number
		remotePort = input("Client-Port: ")
		secondserverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		secondserverSocket.bind((remoteHost, remotePort))
		secondserverSocket.listen(100)
		print "Connecting!"
		setup = 0
	print
	print "Your details"
	print "Host: %s" %(connectHost)
	print "Port: %s" %(connectPort)
	print "Your remote details"
	print "Host: %s" %(remoteHost)
	print "Port: %s" %(remotePort)
	print
	print "Waiting for response..."
	while True:
		serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		serverSocket.connect((connectHost, connectPort))
		tm = serverSocket.recv(64)
		receiveMessage = serverSocket.recv(64)
		serverSocket.close()
		print "Time: %s"%(tm.decode("utf-8"))
		print "Server: %s"%(receiveMessage.decode("utf-8"))
		rawSocket, addr = secondserverSocket.accept()
		message = raw_input("You: ").encode("utf-8")
		renderedMsg = "%s | (H: %s R: %s)" %(message, connectPort, remotePort)
		rawSocket.sendto(renderedMsg, (remoteHost, remotePort))
		rawSocket.close()

#!/usr/bin/env python3

import socket
import select
import time
import sys

BUFFER_SIZE = 4096
LOCAL_HOST = ''

if len(sys.argv) > 1:
	PORT = sys.argv[1]
else:
	PORT = 8000

######## Definierar main loop ###########
def main():
	# The server socket listens to the browser
	print('Listening on port:', str(PORT))
	server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		server_socket.bind((LOCAL_HOST,PORT))
		server_socket.listen(1)
	except socket.error as msg:
		server_socket.close()
		server_socket = None

	if server_socket is None:
		print('Error could not open socket')

	client_socket, addr = server_socket.accept()
	print('Connected by, ', addr)
	server_socket.close()

	while 1:
		data = client_socket.recv(1024)
		if not data: break
		client_socket.send(data)
	client_socket.close()
####### Kör main loop #########
main()

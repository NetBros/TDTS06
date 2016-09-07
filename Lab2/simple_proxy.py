#!/usr/bin/env python3

import socket
import select
import time
import sys
import io

BUFFER_SIZE = 1024
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

	conn, addr = server_socket.accept()
	print('Connected by, ', addr)
	server_socket.close()
	data = ''

	# Getting url from get request
	data_temp = conn.recv(BUFFER_SIZE)
	data += str(data_temp,"utf-8")
	conn.close()

	index_host = "Host: "
	index_pos = data.find(index_host)+ len(index_host)
	n = index_pos
	url_request = ""
	while n < len(data):
		if data[n] == '\n':
			break
		else:
			url_request += data[n]
		n+=1

	print(url_request)



####### Kör main loop #########
main()

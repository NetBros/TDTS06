#!/usr/bin/env python3

import socket, sys
from my_functions import *
#from thread import *

BUFFER_SIZE = 4096
LOCAL_HOST = ''
MAX_CONN = 5

if len(sys.argv) > 1:
	PORT = sys.argv[1]
else:
	PORT = 8000

######## Definierar main loop ###########
def main():
	# The server socket listens to the browser
	print('[*] Listening on port:', str(PORT))
	server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	try:
		server_socket.bind((LOCAL_HOST,PORT))
		server_socket.listen(1)
	except socket.error as msg:
		server_socket.close()
		print("\n[*] Error could not open server socket")
		sys.exit(2)


	conn, addr = server_socket.accept()
	print('Connected by, ', addr)
	server_socket.close()
	data_str = ''

	# Getting url from get request
	data_byte = conn.recv(BUFFER_SIZE)
	data_str += str(data_byte,"utf-8")

	# Finding host address from get request
	url_request = find_url(data_str)

	try:
		client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		client_socket.connect((url_request,80))
		client_socket.send(data_byte)
		while 1:
			data_reply = client_socket.recv(BUFFER_SIZE)
			if (len(data_reply)>0):
				conn.send(data_reply)
			else: break
		client_socket.close()
		conn.close()
	except socket.error as msg:
		client_socket.close()
		print("\n[*] Error could not open client socket")
		sys.exit(2)

####### Kör main loop #########
try:
	main()
except KeyboardInterrupt:
	print("\n[*] Requested keyboard interupt")
	print("[*] Application exiting ...")
	sys.exit()

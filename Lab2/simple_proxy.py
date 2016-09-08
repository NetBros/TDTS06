#!/usr/bin/env python3

import socket, sys
from my_functions import *
#from thread import *

BUFFER_SIZE = 1024
LOCAL_HOST = ''
MAX_CONN = 5

if len(sys.argv) > 1:
	PORT = sys.argv[1]
else:
	PORT = 8000

######## Definierar main loop ###########
def main():
	# The server socket listens to the browser
	print('Listening on port:', str(PORT))
	server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	try:
		server_socket.bind((LOCAL_HOST,PORT))
		server_socket.listen(1)
	except socket.error as msg:
		server_socket.close()
		server_socket = None
		print('Error could not open socket')


	conn, addr = server_socket.accept()
	print('Connected by, ', addr)
	server_socket.close()
	data = ''

	# Getting url from get request
	data_temp = conn.recv(BUFFER_SIZE)
	data += str(data_temp,"utf-8")
	conn.close()

	url_request = find_url(data)

	print(url_request)
#	client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
#	client_socket.connect((url_request,80))
#	client_socket.send("GET / HTTP/1.0%s" % (CRLF))
#
#	while 1:
#		data_temp = client_socket.recv(BUFFER_SIZE)
#		conn.send(data_temp)
#		if not data_temp:break
#
#	conn.close()
#	client_socket.close()




####### Kör main loop #########
try:
	main()
except KeyboardInterrupt:
	print("\n[*] Requested keyboard interupt")
	print("[*] Application exiting ...")
	sys.exit()

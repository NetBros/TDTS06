#!/usr/bin/env python3

from request_handler import *

BUFFER_SIZE = 4096
LOCAL_HOST = ''
MAX_CONN = 1

if len(sys.argv) > 1:
	PORT = sys.argv[1]
else:
	PORT = 8000

temp_list = open("BAN-LIST.txt",'r')
temp_list = temp_list.read()

ban_list = []
for line in temp_list.splitlines():
	line = line.lower()
	line = line.strip()
	ban_list.append(line)

######## Definierar main loop ###########
def main():
	# The server socket listens to the browser
	print('[*] Listening on port:', str(PORT))
	server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	try:
		server_socket.bind((LOCAL_HOST,PORT))
		server_socket.listen(MAX_CONN)
	except socket.error as msg:
		server_socket.close()
		print("\n[*] Error could not open server socket")
		sys.exit(2)

	while 1:
		conn, addr = server_socket.accept()
		print('[*] Connected by, ', addr)
		# Create a new thread to handle request
		new_thread = request_handler(conn,addr,BUFFER_SIZE,ban_list)
		new_thread.start()
	server_socket.close()


####### Kör main loop #########
try:
	main()
except KeyboardInterrupt:
	print("\n[*] Requested keyboard interupt")
	print("[*] Application exiting ...")
	sys.exit()

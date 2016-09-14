#!/usr/bin/env python3

import threading, socket, sys, time
from my_functions import *

class request_handler(threading.Thread):
    def __init__(self,conn,addr,BUFFER_SIZE):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.BUFFER_SIZE = BUFFER_SIZE

    def run(self):
        client_req = ''
        server_req = ''
        timeout = 1
        get_request = self.conn.recv(self.BUFFER_SIZE)
        client_req += str(get_request)
        #test = string(client_req)

        # Finding host address from get request
        host = find_url(client_req)
        #get_request = get_request_close(get_request)

        try:
            print("[*] I'm begining my work in a new thread" )
            client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print("[*] Setting upp connection to ", host)
            client_socket.connect((host,80))
            client_socket.send(get_request)

            TIME_FLAGG = 0
            while 1:
                peek_data = client_socket.recv(self.BUFFER_SIZE,socket.MSG_PEEK)
                peek_bytes = len(peek_data)

                if(peek_bytes>self.BUFFER_SIZE):
                    peek_bytes = self.BUFFER_SIZE
                elif(peek_bytes == 0 and not TIME_FLAGG):
                    TIME_FLAGG = 1
                    start_time = time.time()
                elif(peek_bytes == 0 and ((start_time + timeout) < time.time()) and TIME_FLAGG):
                    break
                elif(peek_bytes > 0 and TIME_FLAGG):
                    TIME_FLAGG = 0

                server_request = client_socket.recv(peek_bytes)
                server_req += str(server_request)
                self.conn.send(server_request)

            client_socket.close()
            self.conn.close()
        except socket.error as msg:
        	client_socket.close()
        	self.conn.close()
        	print("\n[*] Error with socket in thread")
        	sys.exit(2)

        print("[*] I have finished my work in this thread!")

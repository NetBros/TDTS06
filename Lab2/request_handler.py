#!/usr/bin/env python3

import threading, socket, sys, time
from my_functions import *
from array import array

class request_handler(threading.Thread):
    def __init__(self,conn,addr,BUFFER_SIZE):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.BUFFER_SIZE = BUFFER_SIZE

    def run(self):
        get_request = ''
        server_req = ''
        timeout = 1
        byte_get_request = self.conn.recv(self.BUFFER_SIZE)
        print("First byte_get_request",byte_get_request)
        #get_request += str(byte_get_request)
        get_request += str(byte_get_request)
        #test = string(client_req)

        # Finding host address from get request
        host = find_url(get_request)
        print("get_request Keep alive   =>",get_request)
        get_request = get_request_close(get_request)
        print("Get request close    =>",get_request)
        byte_get_request = get_request.encode()
        print("byte_get_request close",byte_get_request)
        #print(host)

        try:
            print("[*] I'm begining my work in a new thread" )
            client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print("[*] Setting upp connection to ", host)
            client_socket.connect((host,80))

            print("[*] Connected, sending get request")
            client_socket.send(byte_get_request)
            print("[*] Get request sent")

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

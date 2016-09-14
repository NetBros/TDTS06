#!/usr/bin/env python3

import threading, socket, sys
from my_functions import *

class request_handler(threading.Thread):
    def __init__(self,conn,addr,BUFFER_SIZE):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.BUFFER_SIZE = BUFFER_SIZE

    def run(self):
        get_request = ''
        server_req = ''
        byte_get_request = self.conn.recv(self.BUFFER_SIZE)
        print("First byte_get_request",byte_get_request)
        get_request += str(byte_get_request)

        #test = string(client_req)

        # Finding host address from get request
        host = find_url(get_request)
        print("get_request Keep alive   =>",get_request)
        get_request = get_request_close(get_request)
        print("Get request close    =>",get_request)
        byte_get_request = get_request.encode('utf-8')

        print("byte_get_request close",byte_get_request)
        #print(host)

        try:
            client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print("[*] Setting upp connection to ", host)
            client_socket.connect((host,80))
            print("[*] Connected, sending get request")
            client_socket.send(byte_get_request)
            print("[*] Get request sent")
            while 1:
                print("[*] Prepering to peek at data")
                peek_data = client_socket.recv(self.BUFFER_SIZE,socket.MSG_PEEK)
                peek_bytes = len(peek_data)
                print("Bytes in recive que",peek_bytes)

                if(peek_bytes>self.BUFFER_SIZE):
                    peek_bytes = self.BUFFER_SIZE
                elif(peek_bytes == 0): break

                server_request = client_socket.recv(peek_bytes)
                #server_req += str(server_request,"utf-8")
                print(server_request)
                self.conn.send(server_request)

            client_socket.close()
            self.conn.close()
        except socket.error as msg:
        	client_socket.close()
        	self.conn.close()
        	print("\n[*] Error could not open client socket")
        	sys.exit(2)

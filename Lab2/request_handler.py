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
        server_req = ""
        byte_get_request = self.conn.recv(self.BUFFER_SIZE)
        get_dict = Get_dict(find_header(byte_get_request)[0])
        host = get_dict["Host"]
        get_dict["Connection"] = "close"
        get_request = dict_2_byte(get_dict)


        try:
            client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print("[*] Setting upp connection to ", host)
            client_socket.connect((host,80))
            client_socket.send(get_request)

            HEADER_FLAGG = 1
            while 1:
                server_request = client_socket.recv(self.BUFFER_SIZE)
                if(len(server_request)<1):break
                if HEADER_FLAGG:
                    server_request_t = find_header(server_request)
                    header_dict = Get_dict(server_request_t[0])
                    body = server_request_t[1]
                    HEADER_FLAGG = 0
                    server_request = b""

                body += server_request
                header = dict_2_byte(header_dict)
            server_request = header + body
            self.conn.send(server_request)

            client_socket.close()
            self.conn.close()
        except socket.error as msg:
        	client_socket.close()
        	self.conn.close()
        	print("\n[*] Error with socket in thread")
        	sys.exit(2)

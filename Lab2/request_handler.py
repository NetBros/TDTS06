#!/usr/bin/env python3

import threading, socket, sys, time
from my_functions import *
from array import array

class request_handler(threading.Thread):
    def __init__(self,conn,addr,BUFFER_SIZE,ban_list):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.BUFFER_SIZE = BUFFER_SIZE
        self.ban_list = ban_list



    def run(self):
        #Checking if the url is free from bad words
        server_req = ""
        byte_get_request = self.conn.recv(self.BUFFER_SIZE)
        get_dict = Get_dict(find_header(byte_get_request)[0])

        try:
            check_ban(get_dict["GET"],1,self.ban_list)
        except My_Error as e:
            print("[*!*] ERROR found ",e.word," in url, redirecting")
            get_dict["Host"] = "www.ida.liu.se"
            temp_get = get_dict["GET"].split(" ")
            get_dict["GET"] = "http://www.ida.liu.se/~TDTS04/labs/2011/ass2/error1.html" + " " + temp_get[1]

            [header, body] = server_conn(get_dict)

            for key in get_dict:
                if key == "Content-Type":
                        if not -1 == header_dict["Content-Type"].find("text/html"):
                            print("Content-Type find------------")
                            try:
                                check_ban(get_dict["GET"],1,self.ban_list)
                            except My_Error as e:
                                print("[*!*] ERROR found ",e.word," in url, redirecting")
                                get_dict["Host"] = "www.ida.liu.se"
                                temp_get = get_dict["GET"].split(" ")
                                get_dict["GET"] = "http://www.ida.liu.se/~TDTS04/labs/2011/ass2/error2.html" + " " + temp_get[1]
                                [header, body] = server_conn(get_dict)

            server_request = header + body

            self.conn.send(server_request)
            self.conn.close()

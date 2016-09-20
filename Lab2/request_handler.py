#!/usr/bin/env python3
from my_functions import *
from array import array
from gzip import decompress

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

        [header_dict, body] = server_conn(get_dict,self.conn,self.BUFFER_SIZE)

        TYPE_FLAGG = 0
        ENCODING_FLAGG = 0
        for key in header_dict:
            if key == "Content-Type":
                TYPE_FLAGG = 1
            elif key == "Content-Encoding":
                ENCODING_FLAGG = 1

        if TYPE_FLAGG:
            if not -1 == header_dict["Content-Type"].find("text/html"):
                    print("Content-Type find------------")
                    try:
                        temp_body = body
                        if ENCODING_FLAGG:
                            if header_dict["Content-Encoding"]=="gzip":
                                temp_body = decompress(body)
                        check_ban(str(temp_body,"utf-8"),2,self.ban_list)
                    except My_Error as e:
                        print("[*!*] ERROR found ",e.word," in url, redirecting")
                        get_dict["Host"] = "www.ida.liu.se"
                        temp_get = get_dict["GET"].split(" ")
                        get_dict["GET"] = "http://www.ida.liu.se/~TDTS04/labs/2011/ass2/error2.html" + " " + temp_get[1]
                        [header_dict, body] = server_conn(get_dict,self.conn,self.BUFFER_SIZE)

        header = dict_2_byte(header_dict)
        server_request = header + body
        self.conn.send(server_request)
        self.conn.close()

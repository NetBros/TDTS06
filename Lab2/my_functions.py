#!/usr/bin/env python3
import string
import collections
import threading, socket, sys, time

def server_conn(get_dict,conn,BUFFER_SIZE):
	#Connects server to client with help of the dictionary from the request sent from our browser
	host = get_dict["Host"]
	get_dict["Connection"] = "close"
	#Finds the host and change from Connection "Keep alive" to Connection "close"
	get_request = dict_2_byte(get_dict)
	try:
		client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		print("[*] Setting upp connection to ", host)
		client_socket.connect((host,80))
		client_socket.send(get_request)
		#Recive the request from the homepage-server and divides to a header and a body
		HEADER_FLAGG = 1
		while 1:
			server_request = client_socket.recv(BUFFER_SIZE)
			if(len(server_request)<1):break
			if HEADER_FLAGG:
				server_request_t = find_header(server_request)
				header_dict = Get_dict(server_request_t[0])
				body = server_request_t[1]
				HEADER_FLAGG = 0
				server_request = b""
			body += server_request
		client_socket.close()
	except socket.error as msg:
		conn.close()
		client_socket.close()
		print("\n[*] Error with client_socket")
		sys.exit(2)
	return(header_dict,body)

#Seperates a get request between "\r\n\r\n" where the header seperates from the body

def find_header(get_request):
	get_request = get_request.split(b"\r\n\r\n")
	return(str(get_request[0],"utf-8"),get_request[1])


#Creates a dictionary from a get request where the first line have nu ":" and then seperates on blank
def Get_dict(get_request):
	my_dict = collections.OrderedDict()
	end_of_line = get_request.find("\r\n")
	Get_request_line = get_request[:end_of_line]
	Get_request_line = Get_request_line.split(" ")
	my_dict[Get_request_line[0]] = Get_request_line[1]+" "+Get_request_line[2]

	for line in get_request[end_of_line+2:].splitlines():
		Get_request_line = line.split(": ")
		my_dict[Get_request_line[0]] = Get_request_line[1]
	return my_dict

# Remakes the get_request from the the dict to a byte array

def dict_2_byte(big_dict):
	LAZY_FLAGG = 1
	get_request = bytearray()
	for key in big_dict:
		value = big_dict[key]
		if LAZY_FLAGG:
			LAZY_FLAGG = 0
			line = key + " " + value
		else:
			line = key + ": " + value
		get_request += line.encode("utf-8") + b"\r\n"
	return(get_request+b"\r\n")


def convert_to_ascii(text):
    return " ".join(str(ord(char)) for char in text)

# Class to send a word as a error
class My_Error(Exception):
     def __init__(self, value,word):
         self.value = value
         self.word = word
# Function to check through the banlist
def check_ban(data,usage,ban_list):
    data = data.lower()
    data = data.strip()
    for word in ban_list:
        if(not -1 == data.find(word)):
            raise My_Error(usage,word)

#!/usr/bin/env python3
import string

def find_url(data):
	host = "Host: "
	index_host_end = data.find(host)+ len(host)
	data = data[index_host_end:]
	end_of_line = data.find("\\r\\n")
	data = data[:end_of_line]

	n = data.find("www.")

	if  n == -1:
		url_request = data
	else:
		k = (n+len("www."))
		url_request = data[k:]

	return url_request

def get_request_close(get_request):
	connection = "Connection: "
	keep_alive = "Keep-Alive"
	close = "close"

	index_first_half = get_request.find(connection)+len(connection)
	print (index_first_half)
	index_second_half = index_first_half+len(keep_alive)

	first_half = get_request[:index_first_half]
	second_half = get_request[index_second_half:]

	return first_half+close+second_half

def convert_to_ascii(text):
    return " ".join(str(ord(char)) for char in text)

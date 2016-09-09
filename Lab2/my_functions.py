#!/usr/bin/env python3
def find_url(data):
	index_host = "Host: "
	index_pos = data.find(index_host)+ len(index_host)
	data = data[index_pos:]
	end_of_line = data.find("\n")
	data = data[:end_of_line]

	n = data.find("www.")

	if  n == -1:
		url_request = data
	else:
		k = (n+len("www."))
		url_request = data[k:]

	url_request = url_request.replace(" ","")
	url_request = url_request.replace("\n","")
	url_request = url_request[:-1]

	return url_request

def convert_to_ascii(text):
    return " ".join(str(ord(char)) for char in text)

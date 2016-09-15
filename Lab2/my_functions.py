#!/usr/bin/env python3
import string
import collections

def find_header(get_request):
	get_request = get_request.split(b"\r\n\r\n")
	header = str(get_request[0],"utf-8")
	body =	get_request[1]
	if len(body) > 0:
		return(header,body)
	elif len(header) == 0:
		return(body)
	else:
		return(header)


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


def dict_2_get(big_dict):
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

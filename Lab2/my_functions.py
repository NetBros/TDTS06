#!/usr/bin/env python3


def find_url(data):
	index_host = "Host: "
	index_pos = data.find(index_host)+ len(index_host)
	data = data[index_pos:]
	end_of_line = data.find("\n")
	data = data[:end_of_line]
#	n = 0
#	url_request = ""
#	find_www = ""
#	clean_url_request= ""
	#print(len(data))

	n = data.find("www.")
	print(n)
	#print(data)
	if  n == -1:
		url_request = data
	else:
		url_request = data[(n+len("www."))]

	url_request = url_request.replace(" ","")
	url_request = url_request.replace("\n","")
	url_request = url_request[:len(data)-1]

	#while n < len(data):
	#	if n == len(data)-1:
	#		break
	#	elif data.find("www.") == -1:
	#		#print("ej WWW")
	#		url_request += data[n]
	#		url_request = clean_url_request
	#	else:
	#		n= data.find("www.")+len("www.")
	#		find_www += data[n]
	#		find_www = clean_url_request
	#	n+=1
	#print(url_request,", ", len(url_request))
	return url_request

#!/usr/bin/env python3


def find_url(data):
	index_host = "Host: "
	index_pos = data.find(index_host)+ len(index_host)
	n = index_pos
	url_request = ""
	find_www = ""
	while n < len(data):
		if data[n] == '\n':
			break
		elif find_www == 'www.':
			url_request += data[n]
		else:
			find_www += data[n]
		n+=1
	clean_url_request = url_request.replace(" ","")
	return clean_url_request

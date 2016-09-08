#!/usr/bin/env python3


def find_url(data):
	index_host = "Host: "
	index_pos = data.find(index_host)+ len(index_host)
	n = index_pos
	url_request = ""
	while n < len(data):
		if data[n] == '\n':
			break
		else:
			url_request += data[n]
		n+=1
	return url_request

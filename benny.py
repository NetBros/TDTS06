#!/usr/bin/env python3

import collections

def Get_dict(data)
    dict = collections.OrderedDict()
    dict = dict()
    first_line = 1
    end_of_get = 0

if first_line = 1
    Get_request_line = get_request.readline()
    Get_request_line = get_request.split()
    dict[Get_request_line[0]] = Get_request_line[1]
    first_line = 0
else
    while get_request[end_of_line:].find("") != -1
        end_of_line = get_request[end_of_line:].find("\n")
        Get_request_line = get_request[end_of_line:].readline()
        Get_request_line = get_request[end_of_line:]
        dict[Get_request_line[0]] = Get_request_line[1]
        end_of_get ++

return dict


for key in dict.keys():
    print(key)

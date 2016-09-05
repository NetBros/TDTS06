#!/usr/bin/env python

import socket
import select
import time
import sys

class My_Server :
	def my_print(self):
		return 'hello world' 
output = My_Server()
print (output.my_print())

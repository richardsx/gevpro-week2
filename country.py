#!/usr/bin/env python
#Richards Zheng


class Country():
	
		def __init__(self, string):
			self.string = string
		
		def __str__(self):
			return "Hello from {}".format(self.string)
		
		


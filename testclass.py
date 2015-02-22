#!/usr/bin/python3
#Richards Zheng

import sys
from country import Country

def main(argv):
	n = (argv[1])
	x = Country(n)
	print(x)
	
if __name__ == "__main__":	
	main(sys.argv)	

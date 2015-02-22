#!/usr/bin/python3
#Richards Zheng

import sys
from country import country


def main(argv):
	if len (argv) == 3:
		# Create country object and print
		a = (argv[1])
		b = (argv[2])
		country1 = country(a)
		country2 = country(b)
		print(country1)
		print(country2)
	else:
		print("The invocation should be: ./testclass.py ", "first country name and", "second country name")
	
if __name__ == "__main__":	
	main(sys.argv)	



		

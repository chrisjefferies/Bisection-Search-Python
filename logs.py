import math
import random

roads_kinds = ' St',' Rd', ' Blvd', ' Ave', ' Ct', ''

# Test behavior of basic logrithmic operations in Python. 
#
#
# confirm Guassian function returns expected data within anticipated range of given values.

def take_log(x):
	print len(roads_kinds)
	print math.log(x)

# take_log(10)

def get_ran(array):
	# Calculate according to Gaussian distribution. 
	e = 2.7182
	a = len(array) - 1
	y = random.random() * (len(array) - 1)
	x = int( math.pow( - a * math.log(y/a) , 0.5) )

	return array[x]

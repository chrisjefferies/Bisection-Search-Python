# How long does it take an art major to figure out how to code a bisection search algorith?


##-- I'm going through those 101 Computer Science lectures from MIT
#
# This kinda works, but it doesn't get closer with every jump, just most of them. 
#
def bisecSearchOne(x):
	"""accepts positive float"""
	assert type(x) == float
	assert x > 1
	# guess at an answer y between 0 and x
	y = x / 2

	##-- The prof introduced the concept at the end of lecture 4
	#
	# as one of those cliffhanger's for next week's installment
	#
	# This is my first attempt. 
	for i in range(1, 100):
		if y * y == x:
			print 'I found it: ', y
			break
		else:
			if y * y > x:
				# y is too big, make it smaller
				y = y - (y / (2 * i))
			else:
				# y is too small
				y = y + (y / (2 * i))
			if (i % 5 == 0):
				print 'still looking. On Try: ', i, 'Guessing: ', y
		


# bisecSearchOne(25.0)

import math
def bisecSearchTwo(x, num):
	"""accepts x as float and num as int"""
	assert type(x) == float and type(num) == int
	assert x > 1
	y = x
	# I fiddled around with arrays for a while, trying to compare the previous jump to this one. 

	#guess = array('f', [x]);
	
	for n in range(0, num):
		#print 'Guess: ', y, 'n-1: ', guess[n - 1]
		if y * y == x:
			print 'I found it: ', y, 'on guess ', n
			break
		else:
			##-- THEN IT FRICKIN CLICKED.
			#
			# when I decided to write the jumps in terms of x. 
			# oh. Huh. That's weird. That looks just like binary! 
			#
			# Oh, and it's about 3 hours, for the record. 
			#
			if y * y > x:
				# y is too big
				y = y - (x / math.pow(2, n))
			else: 
				# y is too small
				y = y + (x / math.pow(2, n))

		#guess.append(y)
		#print y

		
# completes in 56 guesses. 
bisecSearchTwo(25.0, 100)


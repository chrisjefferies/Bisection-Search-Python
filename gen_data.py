import datetime
import random
import names
import math

file = 'assets/data.csv'

# f = open(file, 'r')

date = datetime.datetime.fromtimestamp(
	int( round(random.random() * 100000))
)
orderID = sum(1 for line in open(file)) + 12000000000

total = round(random.random() * 175 + 25, 2)
shipping = abs(round(total * 0.1 + ( random.random() * 10 - 5 ), 2) )
subtotal = round(total - shipping, 2)
first = names.get_first_name()
last = names.get_last_name()

#need to find a way to modify this likelihood mathematically. Quadratic function?
roads_kinds = 'St','St','St','Rd','Rd', 'Blvd', 'Ave', 'Ct', ''

address_one = str(int(round(random.random() * 10000))) + ' ' + names.get_last_name() + ' ' + roads_kinds[ 
	int(round(random.random() * len(roads_kinds))) - 1
]

if int( math.floor(random.random() * 5) ):
	address_two = ''	
else:
	address_two = 'No. ' + str(int(round(random.random() * 100)))



print address_two






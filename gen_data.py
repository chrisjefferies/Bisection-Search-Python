import datetime
import random
import names
import math

file = 'assets/data.csv'

def get_ran(array):
	# Great place to handle rarity logic.
	return array[int(round(random.random() * len(roads_kinds))) - 1]


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


roads_kinds = ' St',' St',' St',' Rd',' Rd', ' Blvd', ' Ave', ' Ct', ''
address_one = str(int(round(random.random() * 10000))) + ' ' + names.get_last_name() +  get_ran(roads_kinds)

units_kinds = 'No. ', 'Unit ', 'Suite ', 'A', 'B', 'C', 'D', 'A-', 'B-', 'C-', 'D-'
if int( math.floor(random.random() * 5) ):
	address_two = ''	
else:
	address_two = get_ran(units_kinds) + str(int(round(random.random() * 100)))



print address_two






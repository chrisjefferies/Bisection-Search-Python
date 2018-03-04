import datetime
import time
import random
import names
import math
from pyzipcode import ZipCodeDatabase
zcdb = ZipCodeDatabase()

file = 'assets/data.csv'

def get_ran(array):
	# Great place to handle rarity among records logic.
	return array[int(round(random.random() * len(array))) - 1]

def ran_chance(n):
	if int( math.floor(random.random() * n) ):
		# Lands here n-1/n times
		return False
	else:
		# Lands here 1/n times
		return True

def create_address():
	first = names.get_first_name()
	last = names.get_last_name()
	roads_kinds = ' St',' St',' St',' Rd',' Rd', ' Blvd', ' Ave', ' Ct', ''
	address_one = str(int(round(random.random() * 10000))) + ' ' + names.get_last_name() +  get_ran(roads_kinds)

	units_kinds = 'No. ', 'Unit ', 'Suite ', 'Ste. ' 'A', 'B', 'C', 'D', 'A-', 'B-', 'C-', 'D-'
	# One in Five contain a unit address
	if ran_chance(5):
		address_two = get_ran(units_kinds) + str(int(round(random.random() * 100)))
	else:
		address_two = ''

	# Brute Force a valid zip code
	found_one = False
	while found_one == False:
		rand_zip = str(int(round(random.random() * 99999)))
		try:
			_zip = zcdb[ rand_zip ]
		except Exception:
			a = True
		else:
			found_one = True

	city = _zip.city
	state = _zip.state

	return str(first+','+last+','+address_one+','+address_two+','+city+','+state+','+rand_zip)

f = open(file, 'r')

# line_l = ast.literal_eval(f)
num_lines = sum(1 for line in f)
orderID = num_lines + 12000000000

# date = last_line.split(',')[0]

with open(file, 'r') as f:
	lines = f.read().splitlines()
	last_line = lines[-1]

# Get Unix Timestamp of last date and add it to the last one.
unix_date = time.mktime(datetime.datetime.strptime(last_line.split(',')[0], '%Y-%m-%d %H:%M:%S').timetuple())

iso_date = datetime.datetime.fromtimestamp(
	int(unix_date) + int( round(random.random() * 100000))
)

# print iso_date


total = round(random.random() * 175 + 25, 2)
shipping = abs(round(total * 0.1 + ( random.random() * 10 - 5 ), 2) )
subtotal = round(total - shipping, 2)
bill_address = create_address()
if ran_chance(10):
	ship_address = create_address()
else:
	ship_address = bill_address






print orderID






























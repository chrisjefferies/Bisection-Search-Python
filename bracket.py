import random

def weighted_random_basketball(iter, group):
	g = float(iter)
	r = random.random()
	if r > 1.0 / (15.0 - g * 2.0 ):
		return group[0]
	else:
		return group[1], 'UPSET!'

def bracket():

	s = [None] * 8
	e = [None] * 8
	w = [None] * 8
	m = [None] * 8
	win = [None] * 32
	k = 0

	tourney = [s, e, w, m]
	
	s[0] = ['UVA', 'UMBC'] 
	s[7] = ['Cri', 'KS'] 
	s[4] = ['Ken', 'Dav'] 
	s[3] = ['Ariz', 'Buff'] 
	s[5] = ['Miami', 'Loy'] 
	s[2] = ['Ten', 'Wri'] 
	s[6] = ['Nev', 'Tex'] 
	s[1] = ['Cin', 'Geo']

	e[0] = ['Vil','Rad'] 
	e[7] = ['VT','Ala'] 
	e[4] = ['WV','MurS'] 
	e[3] = ['Witc','Mars'] 
	e[5] = ['Fl','StBon'] 
	e[2] = ['TxTe','SF Au'] 
	e[6] = ['Ark','But'] 
	e[1] = ['Purd','CSUF']

	w[0] = ['Xav','TxS'] 
	w[7] = ['Misou','FlS'] 
	w[4] = ['OSU','SDS'] 
	w[3] = ['Gonz','UNCG'] 
	w[5] = ['Hou','SanDi'] 
	w[2] = ['Mich','Mont'] 
	w[6] = ['TAM','Prov'] 
	w[1] = ['UNC','Lipsc']
	
	m[0] = ['Kansas','Penn'] 
	m[7] = ['Seton','NCS'] 
	m[4] = ['Clem','NMS'] 
	m[3] = ['Aub','Charl'] 
	m[5] = ['TCU','Syrac'] 
	m[2] = ['MSU','Buckn'] 
	m[6] = ['URI','Oklah'] 
	m[1] = ['Duke','Iona']

	for t in range(0, len(tourney)):
		for n in range(0, 8):
			if n == 0:
				print '===Conference Results==='
			win[k] = weighted_random_basketball(n, tourney[t][n])
			print win[k]
			k += 1

	# for u in range(0, len(win)):

def bracket_round_two():

	s = [None] * 8
	e = [None] * 8
	w = [None] * 8
	m = [None] * 8
	win = [None] * 32
	k = 0

	tourney = [s, w]
	
	s[0] = ['UVA', 'Kansas'] 
	s[7] = ['Fla', 'TxT'] 
	s[4] = ['Ken', 'Ariz'] 
	s[3] = ['Ark', 'Perd'] 
	s[5] = ['Tenn', 'Loya'] 
	s[2] = ['Vil', 'Ala'] 
	s[6] = ['Murr', 'Witch'] 
	s[1] = ['Cin', 'Tex']

	w[0] = ['Xav','FlaS'] 
	w[7] = ['MSU','Syrac'] 
	w[4] = ['Gonz','OSU'] 
	w[3] = ['Duke','URI'] 
	w[5] = ['Mich','SanDi'] 
	w[2] = ['Kan','NCS'] 
	w[6] = ['Aub','Clem'] 
	w[1] = ['UNC','TAM']

	

	for t in range(0, len(tourney)):
		for n in range(0, 8):
			if n == 0:
				print '===Conference Results==='
			win[k] = weighted_random_basketball(n, tourney[t][n])
			print win[k]
			k += 1




def bracket_round_three():

	s = [None] * 8
	e = [None] * 8
	w = [None] * 8
	m = [None] * 8
	win = [None] * 32
	k = 0

	tourney = [s]
	
	s[0] = ['Cin', 'Loya'] 
	s[7] = ['Kansas', 'Aub'] 
	s[4] = ['UVA', 'Ariz'] 
	s[3] = ['Mich', 'TAM'] 
	s[5] = ['TxT', 'Ark'] 
	s[2] = ['Duke', 'Syrac'] 
	s[6] = ['Xav', 'Gonz'] 
	s[1] = ['Vil', 'Murr']


	

	for t in range(0, len(tourney)):
		for n in range(0, 8):
			if n == 0:
				print '===Conference Results==='
			win[k] = weighted_random_basketball(n, tourney[t][n])
			print win[k]
			k += 1


def bracket_round_four():

	s = [None] * 8
	e = [None] * 8
	w = [None] * 8
	m = [None] * 8
	win = [None] * 32
	k = 0

	tourney = [s]
	
	s[0] = ['Data', 'Data'] 
	s[7] = ['Data', 'Data'] 
	s[4] = ['UVA', 'Cin'] 
	s[3] = ['Duke', 'Aub'] 
	s[5] = ['Vil', 'TxT'] 
	s[2] = ['Xav', 'Mich'] 
	s[6] = ['Data', 'Data'] 
	s[1] = ['Data', 'Data']


	

	for t in range(0, len(tourney)):
		for n in range(0, 8):
			if n == 0:
				print '===Conference Results==='
			win[k] = weighted_random_basketball(n, tourney[t][n])
			print win[k]
			k += 1


def final_four():

	s = [None] * 8
	e = [None] * 8
	w = [None] * 8
	m = [None] * 8
	win = [None] * 32
	k = 0

	tourney = [s]
	
	s[0] = ['Data', 'Data'] 
	s[7] = ['UVA', 'Xav'] 
	s[4] = ['Data', 'Data'] 
	s[3] = ['Data', 'Data'] 
	s[5] = ['Data', 'Data'] 
	s[2] = ['Data', 'Data'] 
	s[6] = ['TxT', 'Aub'] 
	s[1] = ['Data', 'Data']


	

	for t in range(0, len(tourney)):
		for n in range(0, 8):
			if n == 0:
				print '===Conference Results==='
			win[k] = weighted_random_basketball(n, tourney[t][n])
			print win[k]
			k += 1




def national_champion():
	# What the heck, let's just go with the underdog. 
	print 'Texas Tech!'


national_champion()



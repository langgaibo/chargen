# coding: utf8
# 朗盖博 2015 v1.2
prompt = '>: '

def novel():
	print '''
1. Human:
	+1 to all stats
2. Dragonborn:
	+2 Str, +1 Cha
3. Dwarf:
	Hill Dwarf: +2 Con, +1 Wis
	Mountain Dwarf: +2 Str, +2 Con
4. Elf:
	High elf: +2 Dex, +1 Int
	Wood elf: +2 Dex, +1 Wis
	Drow: +2 Dex, +1 Cha
	Eladrin: +2 Dex, +1 Int
5. Gnome:
	forest gnome: +1 Dex, +2 Int
	rock gome: +1 Con, +2 Int
6. Halfling:
	lightfoot: +2 Dex, +1 Cha
	stout: +1 Con, +2 Dex
7. Half-elf:
	+2 Cha, +1 to any two stats of your choice
8. Half-orc:
	+2 Str, +1 Con
9. Tiefling:
	+1 Int, +2 Cha

10. Reroll base stats!
99. Quit!
'''

def error_msg():
	print '!!! What the fuck? !!!'
	print 'It looks like you entered some dumb shit, and I gave up.'
	print "Let's try that again.\n"

def dragonborn():
	to_add = [2, 0, 0, 0, 0, 1]
	race = 'Dragonborn'
	print '\n+2 Str, +1 Cha! Put on some lotion, scales!'
	return to_add, race

def dwarfs():
	race = 'Dwarf'
	print '\nFirst: +2 Constitution, beardo!\n'
	print 'Select a subrace!' 
	print '"h" for Hill Dwarf (+1 Wis),'
	print '"m" for Mountain Dwarf (+2 Str), or "q" to quit.'
	subrace = raw_input(prompt)
	if subrace == 'h':
		to_add = [0, 0, 2, 0, 1, 0]
		race = 'Hill Dwarf'
	elif subrace == 'm':
		to_add = [2, 0, 2, 0, 0, 0]
		race = 'Mountain Dwarf'
	elif subrace == 'q':
		exit(0)
	else:
		print '\nWhat? Try again, dickhead.'
		to_add = [0, 0, 0, 0, 0, 0]
	
	return to_add, race

def elfs():
	race = 'Elf'
	print '\n+2 Dex, pointy!\n'
	print 'Select a subrace!'
	print '"h" for High Elf (+1 Int),'
	print '"w" for Wood Elf (+1 Wis),'
	print '"d" for Drow (+1 Cha),'
	print '"e" for Eladrin (+1 Int), or "q" to quit.'
	subrace = raw_input(prompt)
	if subrace == 'h':
		to_add = [0, 2, 0, 1, 0, 0]
		race = 'High Elf'
	elif subrace == 'w':
		to_add = [0, 2, 0, 0, 1, 0]
		race = 'Wood Elf'
	elif subrace == 'd':
		to_add = [0, 2, 0, 0, 0, 1]
		race = 'Drow'
	elif subrace == 'e':
		to_add = [0, 2, 0, 1, 0, 0]
		race = 'Eladrin'
	elif subrace == 'q':
		exit(0)
	else:
		print '\nWhat? Try again, dickhead.'
		to_add = [0, 0, 0, 0, 0, 0]

	return to_add, race

def gnomes():
	race = 'Gnome'
	print '\n+2 Int, Gizmo!\n'
	print 'Select a subrace!'
	print '"f" for Forest Gnome (+1 Dex),'
	print '"r" for Rock Gnome (+1 Con), or "q" to quit.'
	subrace = raw_input(prompt)
	if subrace == 'f':
		to_add = [0, 1, 0, 2, 0, 0]
		race = 'Forest Gnome'
	elif subrace == 'r':
		to_add = [0, 0, 1, 2, 0, 0]
		race = 'Rock Gnome'
	elif subrace == 'q':
		exit(0)
	else:
		print '\nWhat? Try again, dickhead.'
		to_add = [0, 0, 0, 0, 0, 0]

	return to_add, race

def halflings():
	race = 'Halfling'
	print '\n+2 Dex, Samwise!\n'
	print 'Select a subrace!'
	print '"l" for Lightfoot (+1 Cha),'
	print '"s" for Stout (+1 Con), or "q" to quit.'
	subrace = raw_input(prompt)
	if subrace == 'l':
		to_add = [0, 2, 0, 0, 0, 1]
		race = 'Lightfoot clan Halfling'
	elif subrace == 's':
		to_add = [0, 2, 1, 0, 0, 0]
		race = 'Stout clan Halfling'
	elif subrace == 'q':
		exit(0)
	else:
		print '\nWhat? Try again, dickhead.'
		to_add = [0, 0, 0, 0, 0, 0]

	return to_add, race

def half_elf():
	print '\n+2 Cha, you sexy beast!'
	print '\nNow, type the abbrev. name of the first stat to +1 (i.e. "str"):'
	stat1 = raw_input(prompt)
	print "...and the second stat to +1."
	print "YOU CAN'T DOUBLE DOWN or you'll just lose the point!"
	stat2 = raw_input(prompt)
	return stat1, stat2

#todo - find a more elegant way to do this
def upgraydd(stat1, stat2):
	to_add = [0, 0, 0, 0, 0, 0]
	if stat1 == 'str':
		to_add[0] = 1
	elif stat1 == 'dex':
		to_add[1] = 1
	elif stat1 == 'con':
		to_add[2] = 1
	elif stat1 == 'int':
		to_add[3] = 1
	elif stat1 == 'wis':
		to_add[4] = 1
	elif stat1 == 'cha':
		to_add[5] = 1
	else:
		print "What? error typing stat1.\n"

	if stat2 == 'str':
		to_add[0] = 1
	elif stat2 == 'dex':
		to_add[1] = 1
	elif stat2 == 'con':
		to_add[2] = 1
	elif stat2 == 'int':
		to_add[3] = 1
	elif stat2 == 'wis':
		to_add[4] = 1
	elif stat2 == 'cha':
		to_add[5] = 1
	else:
		print "What? error typing stat2.\n"

	return to_add

def	half_orc():
	to_add = [2, 0, 1, 0, 0, 0]
	race = 'Half-orc'
	print '\n+2 Str, +1 Con, you ugly motherfucker!'
	return to_add, race

def human():
	to_add = [1, 1, 1, 1, 1, 1]
	race = 'Human'
	print '\nHumans get +1 across the board! Patriarchs!'
	return to_add, race

def tiefling():
	to_add = [0, 0, 0, 1, 0, 2]
	race = 'Tiefling'
	print '\n+1 Int, +2 Cha, Tinkerbell!'
	return to_add, race
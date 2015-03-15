# coding: utf8
# 朗盖博 2015 v1.4
from sys import exit

prompt = '>: '

version = '1.4'

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

def att_words():
	a_w = [
		'Strength    ',
		'Dexterity   ',
		'Constitution',
		'Intelligence',
		'Wisdom      ',
		'Charisma    ']
	return a_w

def mod_words():
	m_w = []
	for i in range(6):
		word = ' Mod:'
		m_w.append(word.rjust(18, '-'))
	return m_w

def display_MT(modtotal):
	print '\nTotal mods = %i' % modtotal
	
	if modtotal >=3 and modtotal <= 8:
		print 'Decent stats.\n'
	elif modtotal > 8:
		print 'Great stats!\n'
	else:
		print 'Shit stats!\n'

def error_msg():
	print '!!! What the fuck? !!!'
	print 'It looks like you entered some dumb shit, and I gave up.'
	print "Let's try that again.\n"

def not_a_choice():
	to_add = [0, 0, 0, 0, 0, 0]
	return to_add

def quit():
	print '\nDon\'t let the door hit you in the ass!\n'
	exit(0)

def do_over():
	to_add = 'panda'
	race = 'alot'
	return to_add, race

def dragonborn():
	to_add = [2, 0, 0, 0, 0, 1]
	race = 'Dragonborn'
	print '\n+2 Str, +1 Cha! Put on some lotion, scales!'
	return to_add, race

def dwarf():
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
		quit()
	else:
		to_add = not_a_choice()
	
	return to_add, race

def elf():
	race = 'Elf'
	print '\n+2 Dex, pointy!\n'
	print 'Select a subrace!'
	print '"h" for High Elf (+1 Int),'
	print '"w" for Wood Elf (+1 Wis),'
	print '"d" for Drow (+1 Cha), or "q" to quit.'
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
	elif subrace == 'q':
		quit()
	else:
		to_add = not_a_choice()

	return to_add, race

def gnome():
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
		quit()
	else:
		to_add = not_a_choice()

	return to_add, race

def halfling():
	race = 'Halfling'
	print '\n+2 Dex, Samwise!\n'
	print 'Select a subrace!'
	print '"l" for Lightfoot (+1 Cha),'
	print '"s" for Stout (+1 Con), or "q" to quit.'
	subrace = raw_input(prompt)
	if subrace == 'l':
		to_add = [0, 2, 0, 0, 0, 1]
		race = 'Lightfoot Halfling'
	elif subrace == 's':
		to_add = [0, 2, 1, 0, 0, 0]
		race = 'Stout Halfling'
	elif subrace == 'q':
		quit()
	else:
		to_add = not_a_choice()

	return to_add, race

def half_elf():
	race = 'Half-elf'
	statdict = {'str':0, 'dex':1, 'con':2, 'int':3, 'wis':4, 'cha':5}
	stat1 = 0
	stat2 = 0
	print '\n+2 Cha, you sexy beast!'
	print '\nNow, type the abbrev. name of the first stat to +1 (i.e. "str").'
	print 'Get it right or you won\'t get the bonus!'
	first = raw_input(prompt)
	check1 = first in statdict
	
	if check1:
		stat1 = statdict[first]
	else:
		print "What? error typing stat1.\n"
		half_elf()

	print '...and the second stat to +1.'
	second = raw_input(prompt)
	check2 = second in statdict
	#compare
	if check2:
		stat2 = statdict[second]
	else:
		print "What? error typing stat2.\n"
		half_elf()
	to_add = [0, 0, 0, 0, 0, 2]
	to_add[stat1] = to_add[stat1] + 1
	to_add[stat2] = to_add[stat2] + 1
	return to_add, race

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
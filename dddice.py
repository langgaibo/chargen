#coding: utf8
#D&D Dice roller
from sys import exit
from random import randint

print '\nD&D simple dice roller'
print 'Type "666" to exit at any midpoint.'
print 'version 1.1 朗盖博 2015'

globsum = 0
globlist = []

prompt = '>: '

def roll():
	print '\nHow many sides? Or enter 666 to quit, or 888 to quick-roll stats.'
	num_sides = int(input(prompt))
	if num_sides == 666:
		exit(0)
	elif num_sides == 888:
		generate_stats()
		quick_print()
	else:
		roll2(num_sides)

def roll2(num_sides):
	print 'How many dice to roll? Or enter 666 to quit.'
	num_dice = int(input(prompt))
	if num_dice == 666:
		exit(0)
	else:
		global globlist
		globlist = [ randint(1,num_sides) for num_dice in range(0,num_dice)]
		global globsum
		globsum = sum(globlist)
		print globlist
		print 'Total: %i' % globsum
		rolledmenu()

def rolledmenu():
	print 'Add modifier? y/n or "dm" to modify all rolls:'
	choice = raw_input(prompt)
	if 'y' in choice:
		modifier()
	elif 'dm' in choice:
		dmod()
	else:
		roll()
	roll()

def rolledmenu_stats():
	print 'Modify all rolls? y/n or 666 to quit:'
	choice = raw_input(prompt)
	if 'y' in choice:
		dmod_stats()
	elif '666' in choice:
		exit(0)
	else:
		print 'Ok, starting over.\n\n'
		roll()
	roll()

def modifier():
	print 'Enter modifier (precede with "-" for negatives):'
	mod = int(raw_input(prompt))
	modsum = globsum + mod
	print 'Total: %i' % modsum
	roll()

def dmod():
	global globlist
	print 'Enter modifier ("-" for negative):'
	mod = int(raw_input(prompt))
	globlist = [i+mod for i in globlist]
	print 'Modified rolls: %r' % globlist
	modsum = sum(globlist)
	print 'Total: %i' % modsum
	roll()

def dmod_stats():
	global globlist
	print 'Enter modifier ("-" for negative):'
	mod = int(raw_input(prompt))
	globlist = [i+mod for i in globlist]
	print '\n\nNew Stats:\n'
	quick_print()

def basestat():
	baseroll = [randint(1,6) for i in range(0,4)]
	delroll = min(baseroll)
	baseroll.remove(delroll)
	basestat = sum(baseroll)
	return basestat

def generate_stats():
	global globlist
	globlist = None
	globlist = [basestat() for i in range(0,6)]

def modlist():
	stats = globlist
	modlist = []
	for stat in stats:
		if stat == 9:
			mod = -1
			modlist.append(mod)
		else:
			mod = (stat - 10) / 2
			modlist.append(mod)
	global modtotal
	modtotal = sum(modlist)
	return modlist

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
	for i in range(0,6):
		word = ' Mod:'
		m_w.append(word.rjust(18, '-'))
	return m_w

def zip_all():
	s = globlist
	m = modlist()
	a = att_words()
	w = mod_words()
	length = len(a)
	block = zip(a,s,w,m)
	return block

def display_block():
	block = zip_all()
	for line in block:
		temp = []
		for chunk in line:
			temp.append(str(chunk))
		print ' '.join(temp)

def quick_print():
	display_block()
	print '\nTotal mods = %i' % modtotal
	
	if modtotal >=3 and modtotal <= 8:
		print 'Decent stats.\n'
	elif modtotal > 8:
		print 'Great stats!\n'
	else:
		print 'Shit stats!\n'

	rolledmenu_stats()

roll()
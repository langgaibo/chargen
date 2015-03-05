#coding: utf8
#D&D simple character generator

from random import randint
from sys import exit
# I cheated. I got all the data I wanted, but I didn't figure out
# how to present it on my own.
from collections import OrderedDict

prompt = '>: '

def start():
	mainmenu()

def mainmenu():
	print 'Input "r" to roll base stats, or "q" to quit.'
	choice = raw_input(prompt)
	if 'r' in choice:
		stats()
	elif 'q' in choice:
		exit(0)
	else:
		print 'What the fuck are you talking about? Try again.'
		start()

def attlist():
	attlist = ['Strength', 'Constitution', 'Dexterity', 'Wisdom', 
	'Intelligence', 'Charisma']
	return attlist

def basestat():
	baseroll = [randint(1,6) for i in range(0,4)]
	delroll = min(baseroll)
	baseroll.remove(delroll)
	basestat = sum(baseroll)
	return basestat

def stats():
	a = attlist()
	s = [basestat() for i in range(0,6)]
	stats = OrderedDict(zip(a, s))
	modlist = []

	for i in s:
		if i == 9:
			mod = 1
			modlist.append(mod)
		else:
			mod = ((int(i) - 10) / 2)
			modlist.append(mod)
	
	modtotal = sum(modlist)

	if modtotal > 2:
		print '\nStats\n------------'
		for k, v in stats.items():
			print k, v
		print '\nMods\n------------\n%r' % modlist
		print 'Mod total: %i\n' % modtotal
		start()
	else:	
		print 'Stats\n------------'
		for k, v in stats.items():
			print k, v
		print '\nMods\n------------\n%r' % modlist
		print 'Mod total: %i' % modtotal
		print 'Shit Mods! Rerolling!\n' 
		start()

start()

#todo - racial modifiers
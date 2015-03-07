# coding: utf8
'''
I figured out my own ugly zip() function and learned a lot
about passing args properly and converting between lists, 
tuples, and strings.
My goal was to get rid of the OrderedDict function and I did it!
'''
from random import randint
from sys import exit

print 'D&D simple character generator'
print 'version 0.2 朗盖博 2015'

prompt = '>: '

def start():
	mainmenu()

def mainmenu():
	print 'Input "r" to roll base stats, or "q" to quit.'
	choice = raw_input(prompt)
	if 'r' in choice:
		judgement()
	elif 'q' in choice:
		exit(0)
	else:
		print 'What the fuck are you talking about? Try again.'
		start()

def att_words():
	a_w = [
		'Strength    ',
		'Constitution',
		'Dexterity   ',
		'Wisdom      ',
		'Intelligence',
		'Charisma    ']
	return a_w

def mod_words():
	m_w = []
	for i in range(0,6):
		word = ' Mod:'
		m_w.append(word.rjust(18, '-'))
	return m_w

def basestat():
	baseroll = [randint(1,6) for i in range(0,4)]
	delroll = min(baseroll)
	baseroll.remove(delroll)
	basestat = sum(baseroll)
	return basestat

def statlist():
	statlist = [basestat() for i in range(0,6)]
	return statlist

def modlist():
	to_mod = statlist()
	modlist = []
	for stat in to_mod:
		if stat == 9:
			mod = 1
			modlist.append(mod)
		else:
			mod = (stat - 10) / 2
			modlist.append(mod)
	modtotal = sum(modlist)
	return to_mod, modlist, modtotal

def zip_all():
	a = att_words()
	s, m, mt = modlist()
	w = mod_words()
	combined = []
	length = len(a)
	for i in range(length):
		combined.append((a[i], s[i], w[i], m[i]))
	return combined, mt

def final():
	block, modtotal = zip_all()
	for line in block:
		temp = []
		for chunk in line:
			temp.append(str(chunk))
		print ' '.join(temp)
	return modtotal

def judgement():
	print ''
	mt = final()
	print '\nTotal mods = %i' % mt
	if mt >=3 and mt <= 6:
		print 'Decent rolls.\n'
	elif mt > 6:
		print 'Great rolls!\n'
	else:
		print 'Shit rolls!\n'
	start()
'''
def human():
	# +1 to all six ability scores
	# +1 to any two ability scores of your choice

def aasimar():
	# +2 charisma

def dragonborn():
	# +2 Strength, +1 Charisma

def dwarf():
	# Hill Dwarf: +2 constitution, +1 wisdom
	# Mountain Dwarf: +2 Strength, +2 Constitution

def elf():
	# High elf: +2 Dex, +1 Int
	# Wood elf: +2 Dex, +1 Wis
	# Dark elf: +2 Dex, +1 Cha
	# Eladrin: +2 Dex, +1 Int

def gnome():
	# forest gnome: +1 Dex, +2 Int
	# rock gome: +1 Con, +2 Int

def halfling():
	# lightfoot: +2 Dex, +1 Cha
	# stout: +1 Con, +2 Dex

def half-elf():
	# +2 cha, +1 to any 2 scores

def half-orc():
	# +2 Str, +1 Con

def tiefling():
	# +1 int, +2 cha
'''

start()
# coding: utf8
'''To Do:
select_race():
	map choices to a dict, maybe in separate module to import?'''

from random import randint
from sys import exit
import racestats

print '\nD&D simple character generator'
print 'version 1.2 朗盖博 2015\n'

statlist = None
modtotal = 0
race_selected = 0
prompt = '>: '

def basestat():
	baseroll = [randint(1,6) for i in range(0,4)]
	delroll = min(baseroll)
	baseroll.remove(delroll)
	basestat = sum(baseroll)
	return basestat

def generate_stats():
	global statlist
	statlist = None
	statlist = [basestat() for i in range(0,6)]

def select_race():
	global race_selected
	
	if race_selected == 2:
		racestats.error_msg()
		race_selected = 1
	else:
		race_selected = 1

	print 'See the list above to review racial modifiers,'
	print 'then enter a # to select race and apply modifiers:'
	choice = int(raw_input(prompt))

# To Do: Find a way to make this elegant
	if choice == 1:
		to_add, race = racestats.human()
	elif choice == 2:
		to_add, race = racestats.dragonborn()
	elif choice == 3:
		to_add, race = racestats.dwarfs()
	elif choice == 4:
		to_add, race = racestats.elfs()
	elif choice == 5:
		to_add, race = racestats.gnomes()
	elif choice == 6:
		to_add, race = racestats.halflings()
	elif choice == 7:
		stat1, stat2 = racestats.half_elf()
		helf_stats(stat1, stat2)
	elif choice == 8:
		to_add, race = racestats.half_orc()
	elif choice == 9:
		to_add, race = racestats.tiefling()
	elif choice == 10:
		race_selected = 0
		print ' Rerolling!'
		generate_stats()
		judgement()
	elif choice == 99:
		exit(0)
	else:
		print "\nWhat?\n"
		select_race()
	
	add_stats(to_add, race)
	mainmenu()

def add_stats(to_add,race):
	global statlist
	global race_selected
	addlist = to_add
	racename = race
	if addlist == [0, 0, 0, 0, 0, 0]:
		race_selected = 2
		judgement()
	else:
		for i in range(len(statlist)):
			statlist[i] = statlist[i] + addlist[i]
		print '\nFINAL STATS for your %s:' % race
		judgement()

def helf_stats(stat1, stat2):
	global statlist
	global race_selected
	addlist = racestats.upgraydd(stat1, stat2)
	if addlist == [0, 0, 0, 0, 0, 0]:
		race_selected = 2
		judgement()
	else:
		for i in range(len(statlist)):
			statlist[i] = statlist[i] + addlist[i]
		print '\nFINAL STATS for your Half-elf:'
		judgement()

def modlist():
	stats = statlist
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
	s = statlist
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

def display_MT():
	print '\nTotal mods = %i' % modtotal
	
	if modtotal >=3 and modtotal <= 8:
		print 'Decent stats.\n'
	elif modtotal > 8:
		print 'Great stats!\n'
	else:
		print 'Shit stats!\n'

def judgement():
	global race_selected
	
	if race_selected == 1:
		race_selected = 0
		display_block()
		display_MT()
		print 'Starting over!\n'
		mainmenu()
	else:
		racestats.novel()
		display_block()
		display_MT()
		select_race()

def mainmenu():
	print 'Input "r" to roll base stats, or "q" to quit.'
	choice = raw_input(prompt)
	
	if choice == 'r':
		generate_stats()
		judgement()
	elif choice == 'q':
		exit(0)
	else:
		print 'What the fuck are you talking about? Try again.'
		mainmenu()

mainmenu()
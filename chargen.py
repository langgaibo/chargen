# coding: utf8
'''
To Do:
-Clean out all traces of Human Variant (not part of core),
	remove race value from plus_stat since it only applies to one race now.
-Condense the ugly hard-coded choice functions into something that elegantly
selects from within a dictionary or something.
	select_race():
		map choices to a dict, maybe in separate module to import?
	plus_stat():
		there's GOT to be an easy way to just link the attribute strings to
		the proper list index, then iterate and add the appropriate value
		to that index...
'''
from random import randint
from sys import exit
import racestats

print '\nD&D simple character generator'
print 'version 1.1 朗盖博 2015\n'

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

def show_stats():
	judgement()
	select_race()

#todo - push this into a config module, return something easier
def select_race():
	global race_selected
	race_selected = 1
	print 'Scroll up to see core stats, then'
	print 'enter a number to select race and apply modifiers:'
	choice = int(raw_input(prompt))
	if choice == 1:
		human()
	elif choice == 2:
		dragonborn()
	elif choice == 3:
		dwarfs()
	elif choice == 4:
		elfs()
	elif choice == 5:
		gnomes()
	elif choice == 6:
		halflings()
	elif choice == 7:
		half_elf()
	elif choice == 8:
		half_orc()
	elif choice == 9:
		tiefling()
	elif choice == 10:
		race_selected = 0
		print ' Rerolling!'
		generate_stats()
		show_stats()
	elif choice == 99:
		exit(0)
	else:
		print "What?"
		select_race()
	mainmenu()

def stats_review():
	a = att_words()
	s = statlist
	combined = zip(a,s)
	for tup in combined:
		temp = []
		for val in tup:
			temp.append(str(val))
		print ' '.join(temp)

def plus_stat(stat1, stat2):
	global statlist
	addlist = racestats.upgraydd(stat1, stat2)
	for i in range(len(statlist)):
		statlist[i] = statlist[i] + addlist[i]
	print '\nFINAL STATS for your Half-elf:'
	judgement()

def human():
	global statlist
	print '\nHumans get +1 across the board! Patriarchs!'
	statlist = [i + 1 for i in statlist]
	print '\nFINAL STATS for your Human:'
	judgement()

def dragonborn():
	global statlist
	print '\n+2 Str, +1 Cha! Put on some lotion, scales!'
	statlist[0] = statlist[0] + 2
	statlist[5] = statlist[5] + 1
	print '\nFINAL STATS for your Dragonborn:'
	judgement()

def dwarfs():
	global statlist
	print '\nFirst: +2 Constitution, beardo!'
	statlist[2] = statlist[2] + 2
	print 'Select a subrace!' 
	print '"h" for Hill Dwarf, "m" for Mountain Dwarf, or "q" to quit.'
	subrace = raw_input(prompt)
	if subrace == 'h':
		statlist[4] = statlist[4] + 1
		race = 'Hill Dwarf'
	elif subrace == 'm':
		statlist[0] = statlist[0] + 2
		race = 'Mountain Dwarf'
	elif subrace == 'q':
		exit(0)
	else:
		print '\nWhat? Try again, dickhead.'
		statlist[2] = statlist[2] - 2
		dwarfs()

	print '\nFINAL STATS for your %r:' % race
	judgement()

def elfs():
	global statlist
	print '\nFirst: +2 Dex, pointy!'
	statlist[1] = statlist[1] + 2
	print 'Select a subrace!'
	print '"h" for High Elf, "w" for Wood Elf,'
	print '"d" for Drow, "e" for Eladrin, or "q" to quit.'
	subrace = raw_input(prompt)
	if subrace == 'h':
		statlist[3] = statlist[3] + 1
		race = 'High Elf'
	elif subrace == 'w':
		statlist[4] = statlist[4] + 1
		race = 'Wood Elf'
	elif subrace == 'd':
		statlist[5] = statlist[5] + 1
		race = 'Drow'
	elif subrace == 'e':
		statlist[3] = statlist[3] + 1
		race = 'Eladrin'
	elif subrace == 'q':
		exit(0)
	else:
		print '\nWhat? Try again, dickhead.'
		statlist[1] = statlist[1] - 2
		elfs()

	print '\nFINAL STATS for your %r:' % race
	judgement()

def gnomes():
	global statlist
	print '\nFirst: +2 Int, Gizmo!'
	statlist[3] = statlist[3] + 2
	print 'Select a subrace!'
	print '"f" for Forest Gnome, "r" for Rock Gnome, or "q" to quit.'
	subrace = raw_input(prompt)
	if subrace == 'f':
		statlist[1] = statlist[1] + 1
		race = 'Forest Gnome'
	elif subrace == 'r':
		statlist[2] = statlist[2] + 1
		race = 'Rock Gnome'
	elif subrace == 'q':
		exit(0)
	else:
		print '\nWhat? Try again, dickhead.'
		statlist[3] = statlist[3] - 2
		gnomes()

	print '\nFINAL STATS for your %r:' % race
	judgement()

def halflings():
	global statlist
	print '\nFirst: +2 Dex, Samwise!'
	statlist[1] = statlist[1] + 2
	print 'Select a subrace!'
	print '"l" for Lightfoot, "s" for Stout, or "q" to quit.'
	subrace = raw_input(prompt)
	if subrace == 'l':
		statlist[5] = statlist[5] + 1
		race = 'Lightfoot clan Halfling'
	elif subrace == 's':
		statlist[2] = statlist[2] + 1
		race = 'Stout clan Halfling'
	elif subrace == 'q':
		exit(0)
	else:
		print '\nWhat? Try again, dickhead.'
		statlist[1] = statlist[1] - 2
		halflings()

	print '\nFINAL STATS for your %r:' % race
	judgement()

def half_elf():
	global statlist
	print '\nFirst: +2 Cha, you sexy beast!'
	statlist[5] = statlist[5] + 2
	stats_review()
	print '\nNow, type the abbrev. name of the first stat to +1 (i.e. "str"):'
	stat1 = raw_input(prompt)
	print "and the second stat to +1."
	print "YOU CAN'T DOUBLE DOWN or you'll just lose the point!"
	stat2 = raw_input(prompt)
	plus_stat(stat1, stat2)

def	half_orc():
	global statlist
	print '+2 Str, +1 Con, you ugly motherfucker!'
	statlist[0] = statlist[0] + 2
	statlist[2] = statlist[2] + 1
	print '\nFINAL STATS for your Half-orc:'
	judgement()

def tiefling():
	global statlist
	print '+1 Int, +2 Cha, Tinkerbell!'
	statlist[3] = statlist[3] + 1
	statlist[5] = statlist[5] + 2
	print '\nFINAL STATS for your Tiefling:'
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

def judgement():
	global race_selected
	display_block()
	print '\nTotal mods = %i' % modtotal
	
	if modtotal >=3 and modtotal <= 8:
		print 'Decent stats.\n'
	elif modtotal > 8:
		print 'Great stats!\n'
	else:
		print 'Shit stats!\n'
	
	if race_selected == 0:
		racestats.novel()
		select_race()
	else:
		race_selected = 0
		print 'Starting over!\n\n'
		mainmenu()

def mainmenu():
	print 'Input "r" to roll base stats, or "q" to quit.'
	choice = raw_input(prompt)
	
	if choice == 'r':
		generate_stats()
		show_stats()
	elif choice == 'q':
		exit(0)
	else:
		print 'What the fuck are you talking about? Try again.'
		mainmenu()

mainmenu()
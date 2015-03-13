# coding: utf8
from random import randint
import racestats

print '\nD&D simple character generator'
print 'version 1.3 朗盖博 2015\n'

statlist = []
modtotal = 0
race_selected = 0
racedict = {1:'human', 2:'dragonborn', 3:'dwarf', 4:'elf', 5:'gnome',
6:'halfling', 7:'half_elf', 8:'half_orc', 9:'tiefling', 10:'do_over',
99:'quit'}

prompt = '>: '

def basestat():
	baseroll = [randint(1,6) for i in range(4)]
	delroll = min(baseroll)
	baseroll.remove(delroll)
	basestat = sum(baseroll)
	return basestat

def generate_stats():
	global statlist
	#statlist = None
	statlist = [basestat() for i in range(6)]

def selected_check():
	global race_selected
	if race_selected == 2:
		racestats.error_msg()
		race_selected = 1
	else:
		race_selected = 1

def select_race():
	selected_check()
	print 'See the list above to review racial modifiers,'
	print 'then enter the # to select race and apply mods:'
	choice = int(raw_input(prompt))
	check = choice in racedict
	if check == True:
		val = str(racedict[choice])
		wrap = 'to_add, race = racestats.%s()' % val
		exec wrap
		add_stats(to_add, race)
		mainmenu()
	else:
		print "\nWhat?\n"
		select_race()

def reroll():
	global race_selected
	race_selected = 0
	print ' Rerolling!'
	generate_stats()
	judgement()

def add_stats(to_add,race):
	global statlist
	global race_selected
	addlist = to_add
	racename = race
	if addlist == [0, 0, 0, 0, 0, 0]:
		race_selected = 2
		judgement()
	elif addlist == 'panda':
		reroll()
	else:
		for i in range(len(statlist)):
			statlist[i] = statlist[i] + addlist[i]
		print '\nFINAL STATS for your %s:' % race
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
	for i in range(6):
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
		racestats.quit()
	else:
		print 'What the fuck are you talking about? Try again.'
		mainmenu()

mainmenu()
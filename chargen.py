# coding: utf8

from random import randint
import dice_lib

print('\nD&D simple character generator! ')
print('version %s\n' % dice_lib.version)

statlist = []
block = []
modtotal = 0
race_selected = 0
racedict = {1:'human', 2:'dragonborn', 3:'dwarf', 4:'elf', 5:'gnome',
6:'halfling', 7:'half_elf', 8:'half_orc', 9:'tiefling', 88:'do_over',
99:'quit', 666:'quit'}

prompt = '>: '

def basestat():
	baseroll = [randint(1,6) for i in range(4)]
	delroll = min(baseroll)
	baseroll.remove(delroll)
	basestat = sum(baseroll)
	return basestat

def generate_stats():
	global statlist
	statlist = [basestat() for i in range(6)]

def selected_check():
	global race_selected
	if race_selected == 2:
		dice_lib.error_msg()
		race_selected = 1
	else:
		race_selected = 1

def select_race():
	selected_check()
	print('See the list above to review racial modifiers,')
	print('then enter the # to select race and apply mods:')
	choice = int(input(prompt))
	if choice == 66:
		dice_lib.json_block(block)
		select_race()
	elif choice == 77:
		dice_lib.csv_block(block)
		select_race()
	else:
		check_race(choice)

def check_race(choice):
	check = choice in racedict
	if check:
		ldict = {}
		val = racedict[choice]
		wrap = 'to_add, race = dice_lib.%s()' % val
		exec(wrap, globals(),ldict)
		to_add = ldict['to_add']
		race = ldict['race']
		add_stats(to_add, race)
		mainmenu()
	else:
		print("\nWhat?\n")
		select_race()

def reroll():
	global race_selected
	race_selected = 0
	print(' Rerolling!')
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
			statlist[i] += addlist[i]
		print('\nFINAL STATS for your %s:' % race)
		judgement()

def modlist():
	stats = statlist
	modlist = []
	for stat in stats:
		if stat == 9:
			mod = -1
			modlist.append(mod)
		else:
			mod = int((stat - 10) / 2)
			modlist.append(mod)
	global modtotal
	modtotal = sum(modlist)
	return modlist

def zip_all():
	global block
	s = statlist
	m = modlist()
	a = dice_lib.att_words()
	w = dice_lib.mod_words()
	block = list(zip(a,s,w,m))

def display_block():
	zip_all()
	for line in block:
		temp = []
		for chunk in line:
			temp.append(str(chunk))
		attempt = ' '.join(temp)
		print(attempt.center(40))

def output_choice():
	global race_selected
	print("\nSave output? 'n' to skip saving,")
	print("'j' for json, 'c' for csv, or '666' to quit:")

	choice = input(prompt)
	if choice == 'j':
		dice_lib.json_block(block)
		if race_selected == 1:
			race_selected = 0
			reset = 'Starting over!'
			print(reset.center(40, '-'))
			mainmenu()
		else:
			judgement()
	elif choice == 'c':
		dice_lib.csv_block(block)
		if race_selected == 1:
			race_selected = 0
			reset = 'Starting over!'
			print(reset.center(40, '-'))
			mainmenu()
		else:
			judgement()
	elif '666' in choice:
		dice_lib.quit()
	elif choice == 'n':
		print('\nOK, moving on.')
		if race_selected == 1:
			race_selected = 0
			reset = 'Starting over!'
			print(reset.center(40, '-'))
			mainmenu()
		else:
			judgement()
	else:
		dice_lib.error_msg()
		output_choice()

def judgement():
	global race_selected

	if race_selected == 1:
		display_block()
		dice_lib.display_MT(modtotal)
		output_choice()
	else:
		dice_lib.novel()
		display_block()
		dice_lib.display_MT(modtotal)
		select_race()

def mainmenu():
	print('Input "r" to roll base stats, or "q" to quit.')
	choice = input(prompt)

	if choice == 'r':
		generate_stats()
		judgement()
	elif choice == 'q':
		dice_lib.quit()
	else:
		print('What the fuck are you talking about? Try again.')
		mainmenu()

mainmenu()

# coding: utf8
# 朗盖博 2015

from sys import exit
import csv
import json

prompt = '>: '

version = '1.8 朗盖博 2021'

def novel():
	print("""
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

66. Save current stats to JSON!

77. Save current stats to CSV!

88. Reroll base stats!

99. Quit!
""")

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
		m_w.append(word.rjust(8, ' '))
	return m_w

def display_MT(modtotal):
	print('\nTotal mods = %i' % modtotal)

	if modtotal >=3 and modtotal <= 8:
		print('Decent stats.\n')
	elif modtotal > 8:
		print('Great stats!\n')
	else:
		print('Shit stats!\n')

def error_msg():
	print(' ')
	ding = '!!! What the fuck? !!!'
	print(ding.center(40))
	print('It looks like you entered some dumb shit, and I gave up.')
	print("Let's try that again.\n")

def not_a_choice():
	to_add = [0, 0, 0, 0, 0, 0]
	return to_add

def quit():
	print('\nDon\'t let the door hit you in the ass!\n')
	exit(0)

def csv_block(block):
	fo = open("scroll.csv", 'w')
	wr = csv.writer(fo, quoting=csv.QUOTE_ALL)
	for row in block:
		wr.writerow(row)
	fo.close()
	print("\n'scroll.csv' overwritten with latest stats.\n")

def json_block(block):
	f = open("scroll.json", 'w')
	chunk = str(json.dumps(block))
	f.write(chunk)
	f.close()
	print("\n'scroll.json' overwritten with latest stats.\n")

def off_the_bat(bat):
	print(' ')
	print(bat.center(40, '.'))

def do_over():
	to_add = 'panda'
	race = 'Not Selected'
	return to_add, race

def dragonborn():
	to_add = [2, 0, 0, 0, 0, 1]
	race = 'Dragonborn'
	bat = '+2 Str, +1 Cha! Put on some lotion, scales!'
	off_the_bat(bat)
	return to_add, race

def dwarf():
	race = 'Dwarf'
	bat = 'First: +2 Constitution, beardo!'
	off_the_bat(bat)
	print('\nSelect a subrace!')
	print('"h" for Hill Dwarf (+1 Wis),')
	print('"m" for Mountain Dwarf (+2 Str), or "q" to quit.')
	subrace = input(prompt)
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
	bat = '+2 Dex, pointy!'
	off_the_bat(bat)
	print('\nSelect a subrace!')
	print('"h" for High Elf (+1 Int),')
	print('"w" for Wood Elf (+1 Wis),')
	print('"d" for Drow (+1 Cha), or "q" to quit.')
	subrace = input(prompt)
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
	bat = '+2 Int, Gizmo!'
	off_the_bat(bat)
	print('\nSelect a subrace!')
	print('"f" for Forest Gnome (+1 Dex),')
	print('"r" for Rock Gnome (+1 Con), or "q" to quit.')
	subrace = input(prompt)
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
	bat = '+2 Dex, Samwise!'
	off_the_bat(bat)
	print('\nSelect a subrace!')
	print('"l" for Lightfoot (+1 Cha),')
	print('"s" for Stout (+1 Con), or "q" to quit.')
	subrace = input(prompt)
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
	bat = '+2 Cha, you sexy beast!'
	off_the_bat(bat)
	print('\nNow, type the abbrev. name of the first stat to +1 (i.e. "str").')
	first = input(prompt)
	check1 = first in statdict

	if check1:
		stat1 = statdict[first]
	else:
		print("What? error typing stat1.\n")
		to_add = not_a_choice()
		return to_add, race

	print('\n...now type the second stat to +1. DON\'T DOUBLE DOWN!')
	second = input(prompt)
	check2 = second in statdict
	if check2:
		stat2 = statdict[second]
	else:
		print("What? error typing stat2.\n")
		to_add = not_a_choice()
		return to_add, race

	to_add = [0, 0, 0, 0, 0, 2]
	to_add[stat1] += 1
	to_add[stat2] += 1
	if stat1 == stat2:
		taunt1 = 'I warned you, you cheating fuck!'
		taunt2 = 'Original Charisma bonus gone, and...'
		taunt3 = '-2 to %s!' % first
		print(' ')
		print(taunt1.center(40))
		print(taunt2.center(40))
		print(' ')
		print(taunt3.center(40, '.'))
		to_add[5] -= 2
		to_add[stat1] -= 4
		return to_add, race
	else:
		return to_add, race

def	half_orc():
	to_add = [2, 0, 1, 0, 0, 0]
	race = 'Half-orc'
	bat = '+2 Str, +1 Con, you ugly motherfucker!'
	off_the_bat(bat)
	return to_add, race

def human():
	to_add = [1, 1, 1, 1, 1, 1]
	race = 'Human'
	bat = 'Humans get +1 across the board! Patriarchs!'
	off_the_bat(bat)
	return to_add, race

def tiefling():
	to_add = [0, 0, 0, 1, 0, 2]
	race = 'Tiefling'
	bat = '+1 Int, +2 Cha, Tinkerbell!'
	off_the_bat(bat)
	return to_add, race

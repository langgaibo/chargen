#coding: utf8
#D&D Dice roller

import dice_lib
from random import randint

print('\nD&D simple dice roller!')
print('version %s\n' % dice_lib.version)

globlist = []
globsum = 0
modtotal = 0
block = []
prompt = '>: '

def roll():
	print('\nHow many sides? Or enter 666 to quit, or 888 to quick-roll stats.')
	num_sides = int(input(prompt))
	if num_sides == 666:
		dice_lib.quit()
	elif num_sides == 888:
		generate_stats()
		quick_print()
	elif num_sides >= 1001:
		dice_lib.error_msg()
		roll()
	elif num_sides <= 0:
		dice_lib.error_msg()
		roll()
	else:
		roll2(num_sides)

def roll2(num_sides):
	print('How many dice to roll? Or enter 666 to quit.')
	num_dice = int(input(prompt))
	if num_dice == 666:
		dice_lib.quit()
	elif num_dice >= 1001:
		dice_lib.error_msg()
		roll()
	elif num_dice <= 0:
		dice_lib.error_msg()
		roll()
	else:
		global globlist
		globlist = [ randint(1,num_sides) for num_dice in range(0,num_dice)]
		global globsum
		globsum = sum(globlist)
		print(globlist)
		print('Total: %i' % globsum)
		rolledmenu()

def rolledmenu():
	print('Add modifier? y/n or "dm" to modify all rolls:')
	choice = input(prompt)
	if 'y' in choice:
		modifier()
	elif 'dm' in choice:
		dmod()
	else:
		roll()
	roll()

def rolledmenu_stats():
	print('Modify all rolls? y/n or 666 to quit:')
	choice = input(prompt)
	if 'y' in choice:
		dmod_stats()
	elif '666' in choice:
		dice_lib.quit()
	else:
		output_choice()
		roll()
	roll()

def modifier():
	print('Enter modifier (precede with "-" for negatives):')
	mod = int(input(prompt))
	if mod >= 101:
		dice_lib.error_msg()
		roll()
	elif mod <= -101:
		dice_lib.error_msg()
		roll()
	else:
		modsum = globsum + mod
		print('Total: %i' % modsum)
		roll()

def dmod():
	global globlist
	print('Enter modifier ("-" for negative):')
	mod = int(input(prompt))
	if mod >= 101:
		dice_lib.error_msg()
		roll()
	elif mod <= -101:
		dice_lib.error_msg()
		roll()
	else:
		globlist = [i+mod for i in globlist]
		print('Modified rolls: %r' % globlist)
		modsum = sum(globlist)
		print('Total: %i' % modsum)
		roll()

def dmod_stats():
	global globlist
	print('Enter modifier ("-" for negative):')
	mod = int(input(prompt))
	if mod >= 101:
		dice_lib.error_msg()
		roll()
	elif mod <= -101:
		dice_lib.error_msg()
		roll()
	else:
		globlist = [i+mod for i in globlist]
		print('\n\nNew Stats:\n')
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
			mod = int((stat - 10) / 2)
			modlist.append(mod)
	global modtotal
	modtotal = sum(modlist)
	return modlist

def zip_all():
	global block
	s = globlist
	m = modlist()
	a = dice_lib.att_words()
	w = dice_lib.mod_words()
	block = list(zip(a,s,w,m))

def display_block():
	for line in block:
		temp = []
		for chunk in line:
			temp.append(str(chunk))
		print(' '.join(temp))

def output_choice():
	print("\nSave output? 'j' for json, 'c' for csv,")
	print("'n' to move on without saving, or '666' to quit:")
	choice = input(prompt)
	if choice == 'j':
		dice_lib.json_block(block)
	elif choice == 'c':
		dice_lib.csv_block(block)
	elif choice == 'n':
		print("\nOK, moving on.")
		roll()
	elif '666' in choice:
		dice_lib.quit()
	else:
		dice_lib.error_msg()
		output_choice()

def quick_print():
	zip_all()
	display_block()
	dice_lib.display_MT(modtotal)
	rolledmenu_stats()

roll()
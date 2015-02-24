#coding: utf8
#D&D Dice roller
from sys import exit
from random import randint

globrolled = 0
globsum = 0
globlist = []

prompt = '>>> '

def start():
	if globrolled == 0:
		menu()
	else:
		rolledmenu()

def menu():
	print '"r" to roll or "q" to quit:'
	choice = raw_input(prompt)
	if choice == 'r':
		roll()
	elif choice == 'q':
		exit(0)
	else:
		print "I don't understand. Try again."
		start()

def roll():
	print 'How many sides?'
	num_sides = int(input(prompt))
	print 'How many dice to roll?'
	num_dice = int(input(prompt))
	global globlist
	globlist = []
	#list comprehension version:
	#globlist = [ randint(1,num_sides) for num_dice in range(0,num_dice)]
	for num_dice in range(0,num_dice):
		globlist.append(randint(1,num_sides))
	global globsum
	globsum = sum(globlist)
	print globlist
	print 'Total: %i' % globsum
	global globrolled
	globrolled = 1
	start()

def rolledmenu():
	print 'Add modifier? y/n or "dm" to modify all rolls:'
	choice = raw_input(prompt)
	if 'y' in choice:
		modifier()
	elif 'dm' in choice:
		dmod()
	else:
		global globrolled
		globrolled = 0
	start()

def modifier():
	print 'Enter modifier (precede with "-" for negatives):'
	mod = int(raw_input(prompt))
	modsum = globsum + mod
	print 'Total: %i' % modsum
	global globrolled
	globrolled = 0
	start()

def dmod():
	print 'Enter modifier ("-" for negative):'
	mod = int(raw_input(prompt))
	#global globlist
	dmlist = [i+mod for i in globlist]
	print 'Modified rolls: %r' % dmlist
	global globrolled
	globrolled = 0
	start()

print "D&D dice roller\n朗盖博 2015"
start()
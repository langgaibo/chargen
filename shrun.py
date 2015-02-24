#coding: utf8
#Shadowrun Dice Roller
from sys import exit
from random import randint

prompt = ('>>> ')


def start():
	menu()

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
	print 'How many dice to roll?'
	num_dice = int(input(prompt))
	#list comprehension version:
	#x = [ randint(1,6) for num_dice in range(1,num_dice+1)]
	#for loop version:
	x = []
	for num_dice in range(1,num_dice+1):
		x.append(randint(1,6))
	hits = ( x.count(5) + x.count(6) )
	print x
	print 'Hits: %i' % hits
	ones = x.count(1)
	gcount = (float(ones) / num_dice)
	#todo: learn how to pass args from this func to a 'glitch' func
	#for now embed if loop
	if gcount >= 0.5 and hits == 0:
		print '! - Critical Glitch - !'
	elif gcount >= 0.5 and hits > 0:
		print 'Glitch!'
	else:
		start()
	start()

print "Shadowrun dice roller\n朗盖博 2015"
print "Glitches detected automatically. Enjoy!"
start()
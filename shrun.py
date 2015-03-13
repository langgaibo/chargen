#coding: utf8
#Shadowrun Dice Roller
from sys import exit
from random import randint

print '\nShadowrun simple dice roller'
print "Glitches detected automatically. Enjoy!"
print 'version 1.1 朗盖博 2015\n'

prompt = ('>: ')

def roll():
	print 'How many dice to roll? Or type CTRL-C to kill the program'
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
		roll()
	roll()

roll()
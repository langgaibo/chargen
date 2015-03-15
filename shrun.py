#coding: utf8
from sys import exit
from random import randint
import dice_lib

print '\nShadowrun simple dice roller'
print "Glitches detected automatically. Enjoy!"
print 'version %s 朗盖博 2015\n' % dice_lib.version

prompt = ('>: ')

def roll():
	print 'How many dice to roll? Or type CTRL-C to kill the program'
	num_dice = int(input(prompt))
	x = [ randint(1,6) for num_dice in range(1,num_dice+1)]
	print x
	hits(x)
	glitches(x,num_dice)

def hits(x):
	hits = (x.count(5) + x.count(6))
	print 'Hits: %i' % hits

def glitches(x,num_dice):
	ones = x.count(1)
	gcount = (float(ones) / num_dice)
	if gcount >= 0.5 and hits == 0:
		print '! - Critical Glitch - !'
	elif gcount >= 0.5 and hits > 0:
		print 'Glitch!'
	else:
		roll()
	roll()

roll()
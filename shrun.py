#coding: utf8
from random import randint
import dice_lib

print('\nShadowrun simple dice roller!')
print("Glitches detected automatically. Enjoy!")
print('version %s\n' % dice_lib.version)

prompt = ('>: ')

def roll():
	print('How many dice to roll? Or enter 666 to kill the program')
	num_dice = int(input(prompt))
	if num_dice == 666:
		dice_lib.quit()
	elif num_dice > 1000:
		dice_lib.error_msg()
		roll()
	elif num_dice <= 0:
		dice_lib.error_msg()
		roll()
	else:
		x = [randint(1,6) for num_dice in range(1, num_dice+1)]
		print(x)
		hits(x, num_dice)

def hits(x, num_dice):
	hits = (x.count(5) + x.count(6))
	ones = x.count(1)
	print('Hits: %i' % hits)
	print('Ones: %i' % ones)
	gcount = (float(ones) / num_dice)
	if gcount >= 0.5 and hits == 0:
		print('! - Critical Glitch - !')
	elif gcount >= 0.5 and hits > 0:
		print('Glitch!')
	else:
		roll()
	roll()

roll()
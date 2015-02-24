#added commment bitches
#coding: utf8
#D&D simple character generator
import hashmap
from random import randint

stats = hashmap.new()
prompt = '>>> '

def start():
	mainmenu()

def mainmenu():
	print 'Input "r" to roll base stats, or "q" to quit.'
	choice = raw_input(prompt)
	if 'r' in choice:
		starter()
	elif 'q' in choice:
		exit(0)
	else:
		print 'What the fuck are you talking about? Try again.'
		start()

def basestat():
	baseroll = [randint(1,6) for i in range(0,4)]
	print 'debug: baseroll = %r' % baseroll
	delroll = min(baseroll)
	baseroll.remove(delroll)
	print 'debug: baseroll - delroll = %r' % baseroll
	basestat = sum(baseroll)
	print 'debug: basestat = %r' % basestat
	return basestat

def starter():
	bstats = [basestat() for i in range(0,6)]
	print 'debug: bstats built from iterating basestat() into a list returns:'
	print bstats
	#bstats.reverse()
	hashmap.set(stats, 'Str', bstats.pop())
	hashmap.set(stats, 'Con', bstats.pop())
	hashmap.set(stats, 'Dex', bstats.pop())
	hashmap.set(stats, 'Wis', bstats.pop())
	hashmap.set(stats, 'Int', bstats.pop())
	hashmap.set(stats, 'Cha', bstats.pop())
	print 'assign them to the hashmap, then it returns:\n'
	hashmap.list(stats)
	print '\nnow I need to figure out how to enforce order on the dict'
	print 'or pass it to a sorting function\n'
	start()

#def selectrace():

start()
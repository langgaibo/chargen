#added commment bitches
#coding: utf8
#D&D simple character generator
import hashmap
from random import randint
from sys import exit

#Thu Mar  5 00:28:09 UTC 2015
#eliminating "hashmap" function because I think i figured an ugly way to do
#exactly what I want.

stats = hashmap.new()
prompt = '>: '

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

#try to do this without globals
def attlist():
	attdict = {1: 'Strength', 2: 'Constitution', 3: 'Dexterity', 4: 'Wisdom', 
	5: 'Intelligence', 6: 'Charisma'}
	print 'debug %r' % attdict
	return attdict

def basestat():
	baseroll = [randint(1,6) for i in range(0,4)]
	print 'debug: baseroll = %r' % baseroll
	delroll = min(baseroll)
	baseroll.remove(delroll)
	print 'debug: baseroll - delroll = %r' % baseroll
	basestat = sum(baseroll)
	print 'debug: basestat = %r' % basestat
	#Thu Mar  5 01:27:21 UTC 2015
	#tried removing this "return" call and got "none" for bstats list values in starter()
	return basestat

def stats():
	# I get to keep this beautiful list comprehension
	statlist = [basestat() for i in range(0,6)]
	return statlist

'''
def debug():
	#attlist()
	stats()
	exit(0)

'''

def starter():
	bstats = [basestat() for i in range(0,6)]
	print 'debug: bstats built from iterating basestat() into a list returns:'
	print bstats
	print '\n\n\ndebug: just pulling from stats() to get the statlist first:'
	cstats = stats()
	print cstats
	print '\n\n\n'
	#bstats.reverse()
'''
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
'''
#def selectrace():


start()
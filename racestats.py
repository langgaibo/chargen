# coding: utf8
def novel():
	print '''Now to select racial bonuses.
1. Human:
	+1 to all six stats
	+1 to any two stats of your choice
2. Dragonborn:
	+2 Str, +1 Cha
3. Dwarf:
	Hill Dwarf: +2 Con, +1 Wis
	Mountain Dwarf: +2 Str, +2 Con
4. Elf:
	High elf: +2 Dex, +1 Int
	Wood elf: +2 Dex, +1 Wis
	Drow: +2 Dex, +1 Cha
	Eladrin: +2 Dex, +1 Int
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

10. Reroll base stats!
99. Quit!
'''

def upgraydd(stat1, stat2):
	to_add = [0, 0, 0, 0, 0, 0]
	if stat1 == 'str':
		to_add[0] = 1
		return to_add
	elif stat1 == 'dex':
		to_add[1] = 1
		return to_add
	elif stat1 == 'con':
		to_add[2] = 1
		return to_add
	elif stat1 == 'int':
		to_add[3] = 1
		return to_add
	elif stat1 == 'wis':
		to_add[4] = 1
		return to_add
	elif stat1 == 'cha':
		to_add[5] = 1
		return to_add
	else:
		print "What? error typing stat1. Going back.\n"
		return to_add

	if stat2 == 'str':
		to_add[0] = 1
		return to_add
	elif stat2 == 'dex':
		to_add[1] = 1
		return to_add
	elif stat2 == 'con':
		to_add[2] = 1
		return to_add
	elif stat2 == 'int':
		to_add[3] = 1
		return to_add
	elif stat2 == 'wis':
		to_add[4] = 1
		return to_add
	elif stat2 == 'cha':
		to_add[5] = 1
		return to_add
	else:
		print "What? error typing stat1. Going back.\n"
		return to_add
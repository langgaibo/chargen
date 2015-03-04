'''
From ex38 in tutorial, got idea for chargen:

Return Stats in order "Str, Int" or whatever, as a list (or) as a string.
After the dice roll, I could find a way to assign the dice rolls (which could
print in an "implied" order) to an ordered Stat list... maybe by doing it 
behind the scenes by pulling the key (stat) values from dict, ordering them,
then just printing the two lists in a special function after all that!!!


potentially helpful stuff from ex38.py:
'''

# starting list
ten_things = "Apples Oranges Crows Telephone Light Sugar"

# list.split('str') converts a list to a string (not sure how non-space
# 'str' behaves:
stuff = ten_things.split(' ')
print stuff

# 'str'.join(list) converts a list back into a string
print ' '.join(stuff)

# second list:
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# peeling off items from second list and appending to starting list:
while len(stuff) != 10:
	#note: list.pop() REMOVES the popped item from the list!
	next_one = more_stuff.pop()
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)

# list[-x] returns positions counted backwards from the end of a list:
print stuff[-1]

# 'str'.join(list[x:y]) returns a string with the "binder" string between
# returned list values as specified, e.g.
print '#'.join(stuff[3:5])
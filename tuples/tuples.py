places = ('India', 'Russia', 'USA' , 'China')
print(places)
print(len(places))

# Create Tuple With One Item
""" 
To create a tuple with only one item, 
you have to add a comma after the item, 
otherwise Python will not recognize it as a tuple.
"""

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

thistuple5 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple5)




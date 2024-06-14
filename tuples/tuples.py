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

#  Using constructor
thistuple1 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple1)

# Access Tuple items
pets = ('dog', 'cat', 'parrot', 'bird')
print(pets[1])

# Unpack tuples
(dog, cat, bird1, birds) = pets
print(dog)
print(cat)
print(bird1)
print(birds)

# Using Asterisk(*) to unpack
(dog, cat, *birdies) = pets
print(dog)
print(cat)
print(birdies)




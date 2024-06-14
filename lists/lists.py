fruits = ['apple', 'banana', 'mango']

print(fruits)

# Accessing items
print(fruits[0]) # returns first element

print(fruits[-1]) # returns last element

print(fruits[0:2]) # returns element from the specified range

# Change item value
fruits[0] = 'watermelon'
print(fruits)

# Insert items
fruits.insert(1, 'pomagranate')
print(fruits)

# Append items
orange =  'orange'
fruits.append(orange)
print(fruits)

# Extend list
other_fruits = ['tomato', 'kiwi']
fruits.extend(other_fruits)
print(fruits)

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
print('Remove items...')

# Remove specific item
objects = ['pencil', 'eraser', 'sharpner', 'pen', 'book', 'notebook']
objects.remove('pencil')
print(objects)


# Remove specific Index
objects.pop(1)
print(objects)

del objects[0]
print(objects)

# delete entire list
# del objects


# Clear the list
objects.clear()
print(objects)


"""
Loop through lists
"""
print('Loop through lists')

places = ['india', 'japan', 'thailand', 'vietnam']

for x in places:
    print(x)

# Loop through the index numbers
for i in range(len(places)):
    print(places[i])
    
# while loop
i = 0
while i < len(places):
    print(places[i])
    i = i + 1


# Looping using list comprehension
# List Comprehension offers the shortest syntax for looping through lists:

[print(x) for x in places]

new_places = []

for x in places:
    if 'i' in x:
        new_places.append(x)
        
print(new_places)

# shorthand of above code using list comprehension
new_places = [x for x in places if 'i' in x]

print(new_places)

# Sort list Alphanumerically
places.sort()
print(places)

nums = [1, 23, 53, 100, 32, 4]
nums.sort()
print(nums)

# sort decending
nums.sort(reverse=True)
print(nums)

# Copy List

"""
You cannot copy a list simply by typing list2 = list1, because: 
list2 will only be a reference to list1, and changes made in 
list1 will automatically also be made in list2.
"""
print('Copy...')

cars = ['nexon', 'jeep']
cars_copy = cars.copy()
cars.append('hector')
print(cars_copy)

cars_copy_new = list(cars)
cars.extend('thar')
print(cars_copy_new)

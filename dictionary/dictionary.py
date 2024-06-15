person = {
    "name": "John Doe",
    "age": 32,
    "isAlive": True,
    "badHabits": None
}

print(person)

# Access items
print(person['name'])
# or
print(person.get('name'))

# Get keys
print(person.keys())

# Get values
print(person.values())

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.

print(person.items())

print('cars...')

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

# Check if ker exists
if 'brand' in car:
    print('brand exists')
    

""" 
Change Values
"""

cars = {
    "make": "toyota",
    "model": 2023,
    "price": 10000
}

cars['price'] = 20000

print(cars)

cars.update({'price': 30000})

print(cars)

# Add items

cars['color'] = 'black'

print(cars)

cars.update({'kms': 32344})

print(cars)

# Removing items
cars.pop('kms')

print(cars)

cars.popitem() #removes last item 

print(cars)

# Remove using 'del' keyword'

del cars['price']

print(cars)

# 'del' can also delete entire dict

del cars

# this will thorw error because cars dict is deleted
# print(cars)

name = {
    'firstname': 'John',
    'lastname': 'Doe'
}

print(name)
name.clear()
print(name)


# Loop through dictionaries
print('\n Loops.... \n')

objects = {
    "1": "pencil",
    "2": "sharpner",
    "3": "eraser",
    "4": "book",
    "5": "notebook"
}

for i in objects:
    print(objects[i])
    
print('\n Print Values... \n')

for i in objects.values():
    print(i)
    
print('\n Print values... \n')

for i in objects.keys():
    print(i)
    
# Copy dictionary

other_objects = objects.copy()

objects['1'] = 'updated object'

print(other_objects)

# other way of copy is to dict function

new_objects = dict(other_objects)

print(new_objects)

nested_dict = {
    'one': {
        '1': 'pen'
    }
}

print(nested_dict['one']['1'])


# Dictionary methods

# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary








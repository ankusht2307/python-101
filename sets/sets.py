# Set

""" 
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.
"""

items = {'lock', 'key', True, False, 0, None, '', 23}
print(items)

# Access items
for x in items:
    print(x)
    
print('key' in items)

# Add items to a Set
items.add('watch')
print(items)

# Remove items
items.remove('watch')
print(items)

items.discard(0)
print(items)

# Loop through set items
for x in items:
    print(x)
    

# Join Sets

"""
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""
print(1 < 2)
print(1 > 2)


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
  
print(bool("Hello"))
print(bool(15))



# Truthy values

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

print(bool('abc'))
print(bool(123))
print(bool(['Pear', 'Berry']))

# Falsy values

print(bool(''))
print(bool(0))
print(bool(False))
print(bool([]))
print(bool({}))
print(bool(()))


"""
One more value, or object in this case, 
evaluates to False, and that is if you 
have an object that is made from a class 
with a __len__ function that returns 0 or False:
"""


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


x = 200
print(isinstance(x, int))

""" 
Syntax:
    lambda arguments: expression
"""

x = lambda a: a * 10

print(x(5))

y = lambda a, b: a + b

print(y(2,3))

# use lambda as an anonymous function

def myFunc(num):
    return lambda a: a * num

doubler = myFunc(4)

print(doubler(4))
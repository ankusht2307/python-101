# Python Math

""" 
Python has a set of built-in math functions, 
including an extensive math module, that 
allows you to perform mathematical tasks 
on numbers.
"""

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

# abs

""" 
The abs() function returns the absolute 
(positive) value of the specified number:
"""

x = abs(-7.25)

print(x)

# pow

""" 
The pow(x, y) function returns the value 
of x to the power of y (xy).
"""

x_pow = pow(4, 3)

print(x_pow)

# The Math Module

""" 
Python has also a built-in module called
math, which extends the list of 
mathematical functions.

To use it, you must import the math
module:
"""
import math

x_sqrt = math.sqrt(256)

print(x_sqrt)

""" 
The math.ceil() method rounds a number upwards
to its nearest integer, and the math.floor() 
method rounds a number downwards to its 
nearest integer, and returns the result:
"""

x_ceil = math.ceil(1.4)
x_floor = math.floor(1.4)

print(x_ceil)
print(x_floor)


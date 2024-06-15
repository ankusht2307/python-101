def my_func():
    print('Hello from function')
    
my_func()


def get_fullname(fname, lname):
    print(fname + ' ' + lname)
    
get_fullname('John', 'Doe')

# Arbitrary Arguments, *args

""" 
If you do not know how many arguments that
will be passed into your function, add 
a * before the parameter name in the function 
definition.

This way the function will receive a tuple of 
arguments, and can access the items accordingly:
"""

def print_cities(*args):
    print(args)
    
print_cities('India', 'Japan')


# Keyword Arguments

def objects(pen, pencil, eraser):
    print(f'pen is from {pen}')
    print(f'pencil is from {pencil}')
    print(f'eraser is from {eraser}')
    
objects(pencil='doms', eraser='hp', pen='parker')


# Arbitrary keyword arguments, **kwargs

def places(**kwargs):
    print(kwargs)
    
places(hp='shimla', uk='mussoorie')
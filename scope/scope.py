# Python Scope

""" 
A variable is only available from inside the
region it is created. This is called scope.
"""

# Local Scope

""" 
A variable created inside a function belongs 
to the local scope of that function, and can
only be used inside that function.
"""

def local_scope():
  x = 300
  print(x)

local_scope()

# Function Inside Function

""" 
As explained in the example above, the variable
x is not available outside the function, but it
is available for any function inside the function:
"""

def myfunc():
  x = 500
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# Global Scope

""" 
A variable created in the main body of the 
Python code is a global variable and belongs
to the global scope.

Global variables are available from within
any scope, global and local.
"""

y = 900

def my_func():
  print(y)

my_func()

print(y)

# Naming Variables

""" 
If you operate with the same variable name inside
and outside of a function, Python will treat them
as two separate variables, one available in the
global scope (outside the function) and one available
in the local scope (inside the function):
"""
a = True

def naming_variables():
    a = 'a'
    print(a)

naming_variables()
print(a)

# Global Keyword

""" 
If you need to create a global variable, but are
stuck in the local scope, you can use the global
keyword.
The global keyword makes the variable global.
"""

def global_func():
  global z
  z = 100000

global_func()

print(z)

# Nonlocal Keyword

""" 
The nonlocal keyword is used to work with 
variables inside nested functions.

The nonlocal keyword makes the variable
belong to the outer function.
"""


def non_local():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(non_local())
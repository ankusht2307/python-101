# Naming a Module

""" 
You can name the module file whatever 
you like, but it must have the file extension .py
"""

# Re-naming a Module

""" 
You can create an alias when you
import a module, by using the as keyword:
"""

import greet as greetings

greetings.greeting('Thor')

# Built-in Modules

""" 
There are several built-in modules in Python,
which you can import whenever you like.
"""

import platform

print(platform.system())

# Using the dir() Function

""" 
There is a built-in function to list
all the function names (or variable names)
in a module. The dir() function:
"""

print(dir(platform))


# Import From Module

""" 
You can choose to import only parts from
a module, by using the from keyword.
"""

from greet import person

print(person)

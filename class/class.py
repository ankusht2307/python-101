# Python Classes/Objects

"""
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.
"""

class someClass:
    x = 5

print(someClass)

# create an object

num  = someClass()
print(num.x)

# The __init__() Function
"""
The examples above are classes and objects in their simplest form, 
and are not really useful in real life applications.

To understand the meaning of classes we have to 
understand the built-in __init__() function.

All classes have a function called __init__(), 
which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties,
or other operations that are necessary to do when the object is being created:
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person('Jose', 23)

print(p1.name)
print(p1.age)


# The __str__() Function

"""
The __str__() function controls what should be returned when 
the class object is represented as a string.

If the __str__() function is not set, the string representation 
of the object is returned:
"""

class Name:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def __str__(self):
        return f"Fullname: {self.fname} {self.lname}"
    
name1 = Name('John', 'Doe')

print(name1)

# Object methods

class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person1("John", 36)
p1.myfunc()


# The pass Statement
""" 
class definitions cannot be empty, but if you
for some reason have a class definition with no
content, put in the pass statement to avoid getting an error.
"""

class Emp:
    pass







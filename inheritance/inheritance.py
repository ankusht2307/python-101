# Python Inheritance

"""
Inheritance allows us to define a class that inherits all the
methods and properties from another class.

Parent class is the class being inherited from, also called 
base class.

Child class is the class that inherits from another class, 
also called derived class.
"""

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def name(self):
        print(self.fname, self.lname)
        
        
person = Person('John', 'Doe')

person.name()

class Student(Person):
    pass

student = Student('Jane', 'Doe')

student.name()


# Add the __init__() Function

""" 
So far we have created a child class that inherits the properties and methods from its parent.

We want to add the __init__() function to the child class (instead of the pass keyword).
"""

# Note: The __init__() function is called automatically every time the class is being used to create a new object.


class Student(Person):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
student1 = Student('Harry', 'Potter')

student1.name()

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        
student2 = Student('Hermione', 'Granger')

student2.name()

""" 
Now we have successfully added the __init__() function, and kept the inheritance of the parent class,
and we are ready to add functionality in the __init__() function.
"""

# Use the super() Function

# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

student3  = Student('Ronald', 'Weasley')

student3.name()

# Adding Properties and methods

class Hogwards(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year
        
    def welcome(self):
        print('Welcome', self.fname, self.lname, 'to the class of', self.year)

hogwards = Hogwards('Harry', 'Potter', 1991)

hogwards.welcome()
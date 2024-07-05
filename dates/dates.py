import datetime

date = datetime.datetime.now()
print(date.year)
print(date.strftime('%A'))

# Creating Date Objects

""" 
To create a date, we can use the 
datetime() class (constructor) 
of the datetime module.

The datetime() class requires three
parameters to create a date: year,
month, day.
"""

x = datetime.datetime(2024, 5, 17)

print(x)
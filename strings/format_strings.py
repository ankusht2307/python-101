times = 1000

# commented out to run next lines of code.
# statement = 'I watched that movie' + times + 'times.'

"""
This will throw type error coz strings 
can't be combined with number in python
"""
# print(statement)

# F-Strings
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

statement = f"I watched that movie {times} times."

print(statement)


price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

calc_price = f"The price is {20 * 59} dollars"
print(calc_price)
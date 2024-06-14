# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


# Numbers

print(type(5)) # int
print(type(5.0)) # float
print(type(5j)) # complex

# Type Conversion

p = 1    # int
q = 2.8  # float
r = 1j   # complex

#convert from int to float:
a = float(p)

#convert from float to int:
b = int(q)

#convert from int to complex:
c = complex(r)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
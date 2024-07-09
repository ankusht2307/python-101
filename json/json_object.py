import json

# Parse JSON - Convert from JSON to Python

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


# Convert from Python to JSON

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# Convert a Python object containing all the legal data types:

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# Format the Result

""" 
The example above prints a JSON string,
but it is not very easy to read, with
no indentations and line breaks.

The json.dumps() method has parameters
to make it easier to read the result:
"""

print(json.dumps(x, indent=4))

# Use the separators parameter to change the default separator:

print(json.dumps(x, indent=4, separators=(". ", " = ")))


# Order the Result

""" 
The json.dumps() method has parameters to
order the keys in the result:
"""

print(json.dumps(x, indent=4, sort_keys=True))
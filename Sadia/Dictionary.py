thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964,
    "Year": 1977
}
print(thisdict)

print(thisdict["Brand"])

print(len(thisdict))

print(type(thisdict))

# Accessing Dictionary

x = thisdict["Model"]
print(x)
y = thisdict.get("Model")  # Accessing by get method
print(y)

# Get a list of the updated keys:

print(thisdict.keys())
a = thisdict.keys()
print(a)  # before the change
thisdict["color"] = "white"
print(a)  # after change

# get a list of the updated values:

print(thisdict.values())  # before the change
thisdict["Year"] = 2020
print(thisdict.values())  # after the change

# updating by update()
thisdict.update({"Model": "Puma"})
print(thisdict)

# Check if key exist
if "Model" in thisdict:
    print("Yes, 'Model' is one of the keys in the dict dictionary")

# Removing items
thisdict.pop("Model")
print(thisdict)

# Print all Key names in Dictionary

for x in thisdict:
    print(x)

for x in thisdict.keys():  # Using key() method
    print(x)

# Print all Values in Dictionary
for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():  # using values() method
    print(x)

# Copy dictionary using copy() method

mydict = thisdict.copy()
print(mydict)

# Copy dictionary using dict() method

mydict = dict(thisdict)
print(mydict)

# Nested dictionary
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

print(myfamily)

# Add three dictionary into a new dictionary
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

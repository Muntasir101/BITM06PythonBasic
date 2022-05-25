dict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964,
    "Year": 1977
}
print(dict)

print(dict["Brand"])

print(len(dict))

print(type(dict))

# Accessing Dictionary

x = dict["Model"]
print(x)
y = dict.get("Model")  # Accessing by get method
print(y)

# Get a list of the updated keys:

print(dict.keys())
a = dict.keys()
print(a)  # before the change
dict["color"] = "white"
print(a)  # after change

# get a list of the updated values:

print(dict.values())  # before the change
dict["Year"] = 2020
print(dict.values())  # after the change

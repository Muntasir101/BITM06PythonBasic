thistuple = ("apple", "banana", "cherry","apple", "banana")
print(thistuple)

print(thistuple[0])
print(thistuple[-1])
print(thistuple[2:5])
print(thistuple[:3])
print(thistuple[2:])
print(thistuple[-4:-1])

# Check if item exist

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Update tuple
# converting into list
y = list(thistuple)
y.append("mango")
thistuple = tuple(y)
print(thistuple)

# add a tuple to a tuple

y = ("orange",)
thistuple += y

print(thistuple)

# Remove tuple

y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
# * assign the rest of the values as alist called red
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# Add a list of values the tropic variable
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#Loop

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# Join tuple

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
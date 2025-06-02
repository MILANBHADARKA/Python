myTup = (1, 2, 3, 4, 5)

print(len(myTup))  # Getting the length of the tuple
print(myTup[0])  # Accessing the first element of the tuple
# myTup[0] = 10  # This will raise an error because tuples are immutable
print(myTup[0:3])  # Slicing the tuple to get the first three elements
print(myTup[0:])  # Slicing the tuple to get the whole tuple
print(myTup[:3])  # Another way to slice the first three elements
print(myTup[-1])  # Accessing the last element of the tuple


# different between tuples and lists is that tuples are immutable, meaning you cannot change their elements after creation while lists are mutable, meaning you can change their elements after creation.
myD = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Accessing values using keys
print(myD['name'])  # Accessing the value associated with the key 'name'
print(myD['age'])   # Accessing the value associated with the key 'age'
print(myD['city'])  # Accessing the value associated with the key 'city'

# Adding a new key-value pair
myD['country'] = 'USA'  # Adding a new key-value pair

print(myD)  # Printing the dictionary after adding a new key-value pair

# Modifying an existing key-value pair
myD['age'] = 31  # Modifying the value associated with the key 'age'
print(myD)  # Printing the dictionary after modifying a key-value pair

# Removing a key-value pair
del myD['city']  # Removing the key-value pair with the key 'city'
print(myD)  # Printing the dictionary after removing a key-value pair

# Checking if a key exists in the dictionary
print('name' in myD)  # Checking if the key 'name' exists in the dictionary
print('city' in myD)  # Checking if the key 'city' exists in the dictionary

# Iterating over keys
for key in myD:
    print(f"{key}: {myD[key]}")  # Printing each key and its associated value

# Iterating over values
for value in myD.values():
    print(value)  # Printing each value in the dictionary

    
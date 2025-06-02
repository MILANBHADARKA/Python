username = "Milan"

print(len(username))

print(username[0])

# username[0] = 'A'     # This will raise an error because strings are immutable
print(username[0:3])  # Slicing the string to get the first three characters
print(username[0:])   # Slicing the string to get the whole string
print(username[:3])   # Another way to slice the first three characters
print(username[-1])  # Accessing the last character of the string
print(username[-3:])  # Slicing the last three characters of the string
print(username[1:4])  # Slicing from index 1 to 3 (not inclusive of 4)
print(username[1:])   # Slicing from index 1 to the end of the string
print(username[:])    # Slicing the whole string
print(username[::2])  # Slicing with a step of 2, getting every second character
print(username[::-1])  # Reversing the string using slicing
print(username[1:4:2])  # Slicing from index 1 to 3 with a step of 2


print(dir(username))  # Listing all attributes and methods of the string object

print(username.upper())  # Converting the string to uppercase
print(username.lower())  # Converting the string to lowercase
print(username.title())  # Converting the string to title case
print(username.capitalize())  # Capitalizing the first character of the string
print(username.count('a'))  # Counting occurrences of 'a' in the string
print(username.find('a'))  # Finding the index of the first occurrence of 'a'
print(username.index('a'))  # Finding the index of the first occurrence of 'a' (raises error if not found)
print(username.replace('a', 'o'))  # Replacing 'a' with 'o' in the string
print(username.split('a'))  # Splitting the string at 'a' and returning a list
print(username.split())  # Splitting the string by whitespace and returning a list
print(username.strip())  # Removing leading and trailing whitespace from the string
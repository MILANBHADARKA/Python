mylist = [1, 2, 3, 4, 5]

print(len(mylist))  # Getting the length of the list
print(mylist[0])  # Accessing the first element of the list
# mylist[0] = 10  # Modifying the first element of the list
print(mylist[0:3])  # Slicing the list to get the first three elements
print(mylist[0:])  # Slicing the list to get the whole list
print(mylist[:3])  # Another way to slice the first three elements
print(mylist[-1])  # Accessing the last element of the list
print(mylist[-3:])  # Slicing the last three elements of the list
print(mylist[1:4])  # Slicing from index 1 to 3 (not inclusive of 4)
print(mylist[1:])  # Slicing from index 1 to the end of the list
print(mylist[:])  # Slicing the whole list
print(mylist[::2])  # Slicing with a step of 2, getting every second element
print(mylist[::-1])  # Reversing the list using slicing

print(dir(mylist))  # Listing all attributes and methods of the list object

mylist.append(6) # Appending an element to the end of the list
print(mylist)  # Printing the modified list after appending
mylist.extend([7, 8])  # Extending the list with another list
print(mylist)  # Printing the modified list after extending
mylist.insert(0, 0)  # Inserting an element at index 0
print(mylist)  # Printing the modified list after inserting
mylist.remove(3)  # Removing the first occurrence of 3 from the list
print(mylist)  # Printing the modified list after removing an element
mylist.pop()  # Removing and returning the last element of the list
print(mylist)  # Printing the modified list after popping an element
mylist.pop(0)  # Removing and returning the first element of the list
print(mylist)  # Printing the modified list after popping the first element
# mylist.clear()  # Clearing the list, removing all elements
print(mylist)  # Printing the empty list after clearing
print(mylist.count(2))  # Counting occurrences of 2 in the list
# print(mylist.index(2))  # Finding the index of the first occurrence of 2
print(mylist.sort())  # Sorting the list in ascending order
print(mylist)  # Printing the sorted list
mylist.reverse() # Reversing the list in place
print(mylist)  # Printing the reversed list
print(mylist.copy())  # Creating a shallow copy of the list
print(mylist)  # Printing the copied list
print(mylist == [1, 2, 4, 5, 6, 7, 8])  # Checking if the list is equal to another list
print(mylist != [1, 2, 4, 5, 6, 7, 8])  # Checking if the list is not equal to another list

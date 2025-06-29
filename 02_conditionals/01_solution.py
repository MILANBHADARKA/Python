# Age group catagorization


age = int(input("Provide me age : \n"))

# print(age)

if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")

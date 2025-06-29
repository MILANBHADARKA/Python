import datetime

age = int(input("Provide me age : \n"))

ticket = 12 if age >= 18 else 8


if datetime.datetime.now().strftime("%A") == "Wednesday":
    ticket -= 2


print(ticket)
    
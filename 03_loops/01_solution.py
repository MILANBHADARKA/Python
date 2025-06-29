numbers = [1,5,-9,4,-8,6,3,-7,-2,-1,0]
count = 0

for number in numbers:
    if number < 0: 
        count += 1
    else:
        continue

print(count)

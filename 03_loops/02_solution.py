numbers = [1,5,-9,4,-8,6,3,-7,-2,-1,0]
count1 = 0

for number in numbers:
    if(number % 2 == 0):
        count1 += 1
    else:
        continue

print(count1)


n=10
count2 = 0

for i in range(1, n+1):
    if i % 2 == 0:
        count2 += 1
    else:
        continue


print(count2)
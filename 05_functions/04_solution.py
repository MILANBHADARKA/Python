import math

import math

def truncate(number, decimals=5):
    factor = 10 ** decimals
    return math.trunc(number * factor) / factor



def circle(redius):
    area = math.pi * (redius ** 2)
    cer = 2 * math.pi * redius

    return area,cer


a,c = circle(3)

print(truncate(a))
print(c)


